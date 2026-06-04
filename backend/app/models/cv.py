from typing import Optional
from beanie import Document
from pydantic import BaseModel, EmailStr, Field
from datetime import date


class PersonalInfo(BaseModel):
    name: str = ""
    surname: str = ""
    address: str = ""
    birthday: Optional[date] = None
    email: Optional[EmailStr] = None
    phone: str = ""
    github: str = ""
    linkedin: str = ""
    nationality: str = ""
    photo_url: str = ""


class Experience(BaseModel):
    job_title: str = ""
    company: str = ""
    company_type: str = ""
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    description: str = ""


class Education(BaseModel):
    degree: str = ""
    institution: str = ""
    graduation_year: Optional[int] = None


class TechSkill(BaseModel):
    name: str = ""
    level: str = ""


class SoftSkill(BaseModel):
    name: str = ""


class LangSkill(BaseModel):
    lang: str = ""
    overall_lvl: str = ""


class Certification(BaseModel):
    title: str = ""
    issuer: str = ""
    year: Optional[int] = None
    url: str = ""


class Publication(BaseModel):
    title: str = ""
    venue: str = ""
    year: Optional[int] = None
    url: str = ""


class CVProfile(Document):
    label: str = Field(..., description="Short name to identify this CV")
    personal_info: PersonalInfo = Field(default_factory=PersonalInfo)
    experience: list[Experience] = Field(default_factory=list)
    education: list[Education] = Field(default_factory=list)
    tech_skills: list[TechSkill] = Field(default_factory=list)
    soft_skills: list[SoftSkill] = Field(default_factory=list)
    lang_skills: list[LangSkill] = Field(default_factory=list)
    certifications: list[Certification] = Field(default_factory=list)
    publications: list[Publication] = Field(default_factory=list)

    class Settings:
        name = "cv_profiles"
