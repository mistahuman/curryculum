from pydantic import BaseModel
from typing import Optional

from app.models.cv import (
    PersonalInfo, Experience, Education,
    TechSkill, SoftSkill, LangSkill,
    Certification, Publication,
)


class CreateCVProfile(BaseModel):
    label: str
    personal_info: PersonalInfo = PersonalInfo()
    experience: list[Experience] = []
    education: list[Education] = []
    tech_skills: list[TechSkill] = []
    soft_skills: list[SoftSkill] = []
    lang_skills: list[LangSkill] = []
    certifications: list[Certification] = []
    publications: list[Publication] = []


class UpdateCVProfile(BaseModel):
    label: Optional[str] = None
    personal_info: Optional[PersonalInfo] = None
    experience: Optional[list[Experience]] = None
    education: Optional[list[Education]] = None
    tech_skills: Optional[list[TechSkill]] = None
    soft_skills: Optional[list[SoftSkill]] = None
    lang_skills: Optional[list[LangSkill]] = None
    certifications: Optional[list[Certification]] = None
    publications: Optional[list[Publication]] = None


class CVProfileSummary(BaseModel):
    id: str
    label: str
    name: str
    surname: str
