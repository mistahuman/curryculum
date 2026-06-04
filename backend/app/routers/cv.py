from fastapi import APIRouter, HTTPException, status
from fastapi.responses import Response

from app.models.cv import CVProfile
from app.schemas.cv import CreateCVProfile, UpdateCVProfile, CVProfileSummary

router = APIRouter(prefix="/cv", tags=["cv"])


@router.get("/", response_model=list[CVProfileSummary])
async def list_cv_profiles():
    profiles = await CVProfile.find_all().to_list()
    return [
        CVProfileSummary(
            id=str(p.id),
            label=p.label,
            name=p.personal_info.name,
            surname=p.personal_info.surname,
        )
        for p in profiles
    ]


@router.post("/", response_model=CVProfile, response_model_by_alias=False, status_code=status.HTTP_201_CREATED)
async def create_cv_profile(payload: CreateCVProfile):
    profile = CVProfile(**payload.model_dump())
    await profile.insert()
    return profile


@router.get("/{id}", response_model=CVProfile, response_model_by_alias=False)
async def get_cv_profile(id: str):
    profile = await CVProfile.get(id)
    if not profile:
        raise HTTPException(status_code=404, detail=f"CV profile {id} not found")
    return profile


@router.put("/{id}", response_model=CVProfile, response_model_by_alias=False)
async def update_cv_profile(id: str, payload: UpdateCVProfile):
    profile = await CVProfile.get(id)
    if not profile:
        raise HTTPException(status_code=404, detail=f"CV profile {id} not found")
    update_data = {k: v for k, v in payload.model_dump().items() if v is not None}
    await profile.set(update_data)
    return profile


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cv_profile(id: str):
    profile = await CVProfile.get(id)
    if not profile:
        raise HTTPException(status_code=404, detail=f"CV profile {id} not found")
    await profile.delete()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/{id}/export")
async def export_cv_profile(id: str):
    profile = await CVProfile.get(id)
    if not profile:
        raise HTTPException(status_code=404, detail=f"CV profile {id} not found")
    json_bytes = profile.model_dump_json(indent=2).encode()
    filename = f"cv-{profile.label.lower().replace(' ', '-')}.json"
    return Response(
        content=json_bytes,
        media_type="application/json",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )


@router.post("/import", response_model=CVProfile, response_model_by_alias=False, status_code=status.HTTP_201_CREATED)
async def import_cv_profile(payload: CreateCVProfile):
    profile = CVProfile(**payload.model_dump())
    await profile.insert()
    return profile
