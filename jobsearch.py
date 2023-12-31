from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
# importing libraries to plot the wordcloud
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

import parameters

# Variables
## Linkedin ID and PASSWORD
email = parameters.username
password = parameters.password

## Write here the job position and local for search
position = "data analyst"
local = "tunisia"

##example below:
## position = "data scientist"
## local = "brazil"

## formating to linkedin model
position = position.replace(' ', "%20")

# Open browser
driver_path = "chromedriver.exe"
driver = webdriver.Chrome()
# Maximizing browser window to avoid hidden elements
driver.set_window_size(1024, 600)
driver.maximize_window()

# Opening linkedin website
driver.get('https://www.linkedin.com/login')
# waiting load
time.sleep(5)

# Search for login and password inputs, send credentions
driver.find_element(By.ID, 'username').send_keys(email)
driver.find_element(By.ID, 'password').send_keys(password)
driver.find_element(By.ID, 'password').send_keys(Keys.RETURN)

# Opening jobs webpage
driver.get(
    f"https://www.linkedin.com/jobs/search/?currentJobId=2662929045&geoId=106057199&keywords={position}&location={local}")
# waiting load
time.sleep(10)

# creating a list where the descriptions will be stored
disc_list = []

for i in range(1, 41):
    # click button to change the job list
    print(f'Page {i}')
    driver.find_element(By.XPATH, f'//button[@aria-label="Página {i}"]').click()
    time.sleep(4)

    # each page show us some jobs, sometimes show 25, others 13 or 21 ¯\_(ツ)_/¯
    jobs_lists = driver.find_element(By.CLASS_NAME,
                                     'scaffold-layout__list-container')  # here we create a list with jobs

    jobs = jobs_lists.find_elements(By.CLASS_NAME,
                                    'jobs-search-results__list-item')  # here we select each job to count

    # waiting load
    time.sleep(4)
    # the loop below is for the algorithm to click exactly on the number of jobs that is showing in list
    # in order to avoid errors that will stop the automation

    for job in range(1, len(jobs) + 1):
        print(f'Job {job}')
        # job click
        driver.find_element(By.XPATH,
                            f'/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[1]/div/ul/li[{job}]').click()
        time.sleep(3)
        driver.find_element(By.XPATH,
                            f'/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[1]/div/ul/li[{job}]/div/div[1]/div[1]/div[2]/div[1]/a').click()
        # waiting load
        time.sleep(3)
        # select job description
        job_desc = driver.find_element(By.ID, 'job-details')
        # get text
        soup = BeautifulSoup(job_desc.get_attribute(
            'outerHTML'), 'html.parser')
        # add text to list
        disc_list.append(soup.text)

# Creating a Dataframe with list
df = pd.DataFrame(disc_list)

# deleting useless words
word_list = ['Expect', 'Qualifications', 'Required', 'expected', 'Responsibilities', 'Requisitos', 'Requirements',
             'Qualificações', 'QualificationsRequired1', 'você deve ter:', 'experiência', 'você:',
             'Desejável', 'great', 'Looking For', 'll Need', 'Conhecimento', 'se:', 'habilidades', 'se:', 'REQUISITOS']
# deleting useless words
df = df.replace(f'\n', '', regex=True)

for i in range(0, len(word_list)):
    df = df.replace(f'^.*?{word_list[i]}', '', regex=True)

# setup wordcloud
stopwords = set(STOPWORDS)
# selecting useless words
badwords = {'gender', 'experience', 'application', 'Apply', 'salary', 'todos', 'os', 'company', 'identity', 'sexual',
            'orientation',
            'de', 'orientação', 'sexual', 'gênero', 'committed', 'toda', 'client', 'conhecimento',
            'world', 'year', 'save', 'São', 'Paulo', 'information', 'e', 'orientação', 'sexual', 'equal', 'oppotunity',
            'ambiente', 'will',
            'Experiência', 'national origin', 'todas', 'work', 'de', 'da', 'years', 'pessoa', 'clients', 'Plano',
            'creating',
            'employer', 'saúde', 'em', 'working', 'pessoas', 'mais', 'data', 'people', 'dia', 'one', 'knowledges',
            'plataforma',
            'ou', 'benefício', 'para', 'software', 'opportunity', 'tecnologia', 'você', 'mais', 'solution', 'national',
            'origin',
            'trabalhar', 'option', 'negócio', 'empresa', 'o', 'sicence', 'team', 'é', 'veteran', 'status', 'etc',
            'raça', 'cor', 'belive',
            'nossa', 'uma', 'como', 'Scientist', 'ferramenta', 'projeto', 'que', 'job', 'benefícios', 'knowledge',
            'toll', 's', 'modelo',
            'desconto', 'cultura', 'serviço', 'time', 'se', 'solutions', 'mercado', 'das', 'somos', 'problema', 'mundo',
            'race', 'color',
            'vaga', 'pelo', 'ser', 'show', 'Seguro', 'Se', 'um', 'Um', 'tool', 'regard', 'without', 'make', 'ao',
            'técnica', 'life',
            'interested', 'diversidade', 'proud', 'ability', 'sobre', 'options', 'using', 'área', 'nosso', 'na', 'seu',
            'product', 'produto',
            'building', 'skill', 'model', 'religion', 'Share', 'receive', 'consideration', 'Aqui', 'vida',
            'ferramentas', 'Vale', 'Refeição',
            'Strong', 'Pay', 'range', 'available', 'part', 'trabalho', 'Alimentação', 'employment', 'qualified',
            'applicants', 'gympass',
            'está', 'comprometida', 'forma', 'Transporte', 'Yes', 'gente', 'melhor', 'lugar', 'believe', 'moment',
            'próximo', 'deasafio',
            'dos', 'oportunidade', 'idade', 'new', 'Try', 'Premium', 'deficiência', 'sempre', 'criar', 'employee',
            'problemas', 'unavailable',
            'Brasil', 'dado', 'hiring', 'trends', 'equipe', 'recent', 'temos', 'build', 'career', 'nós', 'diferencial',
            'ma',
            'total', 'oferecemos', 'contato', 'tem', 'não', 'free', 'Full', 'global', 'computer', 'crossover', 'great',
            'plus', 'customer', 'sua', 'including'
                                       'per week', 'help', 'including', 'check', 'grow', 'day', 'Cliente', 'Customer',
            'processo', 'position', 'email', 'e-mail', 'platform', 'application'}

# deleting the useless words on plot
stopwords.update(badwords)

# plot parameters
wordcloud = WordCloud(background_color='black',
                      width=1600, height=800,
                      stopwords=stopwords,
                      max_words=100,
                      max_font_size=250,
                      random_state=42).generate("".join(df[0]))

# Plot
plt.tight_layout(pad=0)
plt.imshow(wordcloud, interpolation='bilinear')
plt.savefig('wordcloud-job.png', dpi=300)
plt.axis("off")

# exporting our dataframe to a csv file
df.to_csv('wordcloud-job.csv', sep=';')