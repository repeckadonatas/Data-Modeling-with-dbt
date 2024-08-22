"""
Constants that are used throughout the project.
"""

import logging
from pathlib import Path
from datetime import datetime


# DATE
DATE_TODAY = datetime.today().strftime('%Y_%m_%d')
DATETIME_NOW = datetime.now().strftime("%Y%m%d_%H%M")


# FOR LOGGER ONLY
LOG_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

FORMATTER = logging.Formatter(f'{LOG_TIME} :: %(name)s :: %(levelname)s :: %(funcName)s :: %(message)s')
PATH_TO_LOGS = Path(__file__).cwd()
LOG_FILE = PATH_TO_LOGS / 'logs/' / ("app_logger_" + datetime.today().strftime("%Y%m%d") + ".log")


# DATABASE INITIALIZATION
INIT_DB = Path(__file__).cwd() / 'sql/init.sql'

# PG_DUMP FOR BACKUP FUNCTIONALITY
# PG_DUMP = r'C:\Program Files\PostgreSQL\16\bin\pg_dump.exe'
PG_DUMP = 'pg_dump'


# PATHS TO DATA AND FILES
PATH_TO_DATA_STORAGE = Path(__file__).cwd() / 'src/data'

# BACKUPS LOCATION
PATH_TO_BACKUPS = Path(__file__).cwd() / 'backups'
BACKUP_FOLDER_TODAY = PATH_TO_BACKUPS / f"backup_{DATE_TODAY}"

# BACKUP FOLDERS FOR DATABASE
DB_BACKUP_FILE = BACKUP_FOLDER_TODAY / f"db_backup_{DATETIME_NOW}.sql"


# FOR DATAFRAME
COLS_NORMALIZE = ['jobs']

REGION_COLUMN = ['locationRestrictions', 'jobGeo', 'candidate_required_location']

REGIONS = {
    'Europe': ['Europe', 'Albania', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan',
               'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia',
               'Cyprus', 'Czechia', 'Denmark', 'Estonia', 'Finland',
               'France', 'Georgia', 'Germany', 'Greece', 'Hungary',
               'Iceland', 'Ireland', 'Italy', 'Kazakhstan', 'Kosovo',
               'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta',
               'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'North Macedonia',
               'Norway', 'Poland', 'Portugal', 'Romania', 'Russia',
               'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain',
               'Sweden', 'Switzerland', 'Turkey', 'Ukraine', 'United Kingdom',
               'UK', 'Vatican City'],
    'North America': ['Antigua and Barbuda', 'Bahamas', 'Barbados', 'Belize', 'Canada',
                      'Costa Rica', 'Cuba', 'Dominica', 'Dominican Republic', 'El Salvador',
                      'Grenada', 'Guatemala', 'Haiti', 'Honduras', 'Jamaica',
                      'Mexico', 'Nicaragua', 'Panama', 'Saint Kitts and Nevis', 'Saint Lucia',
                      'Saint Vincent and the Grenadines', 'Trinidad and Tobago', 'United States of America ',
                      'USA', '  USA'],
    'South America': ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia',
                      'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname',
                      'Uruguay', 'Venezuela'],
    'Asia': ['Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh',
             'Bhutan', 'Brunei', 'Cambodia', 'China', 'Cyprus',
             'Georgia', 'India', 'Indonesia', 'Iran', 'Iraq',
             'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait',
             'Kyrgyzstan', 'Laos', 'Lebanon', 'Malaysia', 'Maldives',
             'Mongolia', 'Myanmar', 'Nepal', 'North Korea', 'Oman',
             'Pakistan', 'Palestine', 'Philippines', 'Qatar', 'Saudi Arabia',
             'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Taiwan',
             'Tajikistan', 'Thailand', 'Timor-Leste', 'Turkey', 'Turkmenistan',
             'United Arab Emirates', 'UAE', 'Uzbekistan', 'Vietnam', 'Yemen'],
    'Oceania': ['Australia', 'Fiji', 'Kiribati', 'Marshall Islands', 'Micronesia',
                'Nauru', 'New Zealand', 'Palau', 'Papua New Guinea', 'Samoa',
                'Solomon Islands', 'Tonga', 'Tuvalu', 'Vanuatu'],
    'Africa': ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso',
               'Burundi', 'Cabo Verde', 'Cameroon', 'Central African Republic', 'Chad',
               'Comoros', 'Democratic Republic of the Congo', 'Republic of the Congo', "Cote d'Ivoire",
               'Djibouti', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Eswatini',
               'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea',
               'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia', 'Libya',
               'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius',
               'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria',
               'Rwanda', 'Sao Tome and Principe', 'Senegal', 'Seychelles', 'Sierra Leone',
               'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Tanzania',
               'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe']
}

COLUMN_RENAME_MAP = {
    "title": "job_title",
    "title_0": "job_title",
    "jobTitle": "job_title",
    "companyName": "company_name",
    "companyName_0": "company_name",
    "applicationLink": "job_ad_link",
    "applicationLink_0": "job_ad_link",
    "url": "job_ad_link",
    "minSalary": "min_salary",
    "min_salary_annual": "min_salary",
    "annualSalaryMin": "min_salary",
    "maxSalary": "max_salary",
    "max_salary_annual": "max_salary",
    "annualSalaryMax": "max_salary",
    "salaryCurrency": "salary_currency",
    "pubDate": "pub_date_timestamp",
    "publication_date": "pub_date_timestamp",
    "expiryDate": "expiry_date_timestamp",
    0: "region",
    "0": "region",
    "jobGeo": "region",
    "jobGeo_0": "region",
    "jobGeo_1": "region",
    "jobGeo_2": "region",
    "jobType": "job_type",
    "employmentType": "job_type"
}

COMMON_TABLE_SCHEMA = [
    'job_title',
    'company_name',
    'job_type',
    'region',
    'salary',
    'min_salary',
    'max_salary',
    'salary_currency',
    'pub_date_timestamp',
    'expiry_date_timestamp',
    'timestamp',
    'job_ad_link'
]

STR_TO_FLOAT_SCHEMA = [
    'salary'
    'min_salary',
    'max_salary'
]

DATETIME_COLUMNS = ['pub_date_timestamp', 'expiry_date_timestamp']

# TABLES FOR DB
TABLES_TO_CREATE = [
    'remotive_data',
    'himalayas_data',
    'jobicy_data'
]

STAGING_TABLE = 'staging_jobs_listings_data'

CLEAN_DATA_TABLE = 'jobs_listings_data'

SCHEMAS_IN_DB = ['public', 'staging']
