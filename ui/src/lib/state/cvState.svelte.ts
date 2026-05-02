export type PersonalInfo = {
    name: string;
    surname: string;
    address: string;
    tax_code: string;
    birthday: string;
    email: string;
    phone: string;
    github: string;
    linkedin: string;
    gender: string;
    nationality: string;
    url_pic: string;
};

export type Experience = {
    id: string;
    job_title: string;
    company: string;
    company_type: string;
    start_date: string;
    end_date: string;
    description: string;
};

export type Education = {
    id: string;
    degree: string;
    institution: string;
    graduation_year: number | '';
};

export type SkillItem = {
    id: string;
    degree?: string; 
    lang?: string; 
    speaking_lvl?: string;
    writing_lvl?: string;
    listening_lvl?: string;
    comprehension_level?: string;
    overall_lvl?: string;
    driving_license?: string;
};

export type CVData = {
    personal_info: PersonalInfo;
    experience: Experience[];
    education: Education[];
    skills: {
        tech_skills: SkillItem[];
        soft_skills: SkillItem[];
        lang_skills: SkillItem[];
        driving_skills: SkillItem[];
    };
    options: {
        cvlanguage: string;
    };
};

export const cvState = $state<CVData>({
    personal_info: {
        name: "",
        surname: "",
        address: "",
        tax_code: "",
        birthday: "",
        email: "",
        phone: "",
        github: "",
        linkedin: "",
        gender: "",
        nationality: "",
        url_pic: ""
    },
    experience: [],
    education: [],
    skills: {
        tech_skills: [],
        soft_skills: [],
        lang_skills: [],
        driving_skills: []
    },
    options: {
        cvlanguage: "en"
    }
});
