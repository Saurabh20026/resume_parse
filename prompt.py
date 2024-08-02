import openai

openai.api_key = 'your-api-key'


def read_resume(file_path):
    with open(file_path, 'r') as file:
        resume_content = file.read()
    return resume_content


resume_content = read_resume('saurabh_resume.txt')

# prompt for the API
prompt = f"""

You are an AI assistant specialized in parsing resumes. Your task is to convert the resume content provided below into a structured JSON format. Follow these guidelines: 
1. Extract key sections such as Personal Information, Education, Work Experience, Skills, and any other relevant sections present in the resume. 
2. For each section, create appropriate JSON objects and arrays to represent the information. 
3. Ensure that dates, job titles, company names, and other important details are correctly captured. 
4. If there are multiple entries (e.g., multiple jobs or educational qualifications), represent them as arrays of objects. 
5. Use consistent key names throughout the JSON structure. 
6. If any information is unclear or missing, use null values or omit the field rather than making assumptions.
Here's the resume content to parse:

{resume_content}

Please provide the parsed resume in valid JSON format.

"""

# Call the OpenAI API 
response = openai.Completion.create(
    engine="text-davinci-004",
    prompt=prompt,
    max_tokens=1000,
    n=1,
    stop=None,
    temperature=0.5,
)

# Extract and print the JSON output
json_output = response.choices[0].text.strip()
print(json_output)
