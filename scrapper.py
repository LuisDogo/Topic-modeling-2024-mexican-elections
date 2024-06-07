from urllib.request import urlopen
import re

def htmlcode(url):
    return urlopen(url).read().decode("utf-8")


url = "https://centralelectoral.ine.mx/2024/04/08/version-estenografica-del-primer-debate-entre-las-candidaturas-a-la-presidencia-de-la-republica-del-proceso-electoral-federal-2023-2024-la-sociedad-que-queremos/"

