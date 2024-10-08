import json
from pydantic import BaseModel, EmailStr, ValidationError
from typing import List, Optional
from datetime import date
from app.utils import import_cvdata 
import os


class Options(BaseModel):
    cvlanguage: str

class PersonalInfo(BaseModel):
    name: str
    surname: str
    address: str
    tax_code: str
    birthday: date
    email: EmailStr
    phone: str
    github: str
    linkedin: str
    gender: str
    nationality: str
    url_pic: str

class Experience(BaseModel):
    job_title: str
    company: str
    company_type: str
    start_date: date
    end_date: Optional[date]  
    description: str

class Education(BaseModel):
    degree: str
    institution: str
    graduation_year: int

class TechSkill(BaseModel):
    degree: str

class SoftSkill(BaseModel):
    degree: str

class LangSkill(BaseModel):
    lang: str
    speaking_lvl: str
    writing_lvl: str
    listening_lvl: str
    comprehension_level: str
    overall_lvl: str

class DrivingSkill(BaseModel):
    driving_license: str


class Skills(BaseModel):
    tech_skills: List[TechSkill]
    soft_skills: List[SoftSkill]
    lang_skills: List[LangSkill]
    driving_skills: List[DrivingSkill]


class CVData(BaseModel):
    # personal info
    personal_info: PersonalInfo
    # experience
    experience: List[Experience]
    # education
    education: List[Education]
    # skills
    skills: Skills
    # options
    options: Options

    
try:
    data_dict = import_cvdata(os.path.join("mycv", "mycv-demo.json"))
    cv_data = CVData.model_validate(data_dict)
    print(f"Validated! \n{cv_data.model_dump()}") 
except ValidationError as e:
    print(e.json())
