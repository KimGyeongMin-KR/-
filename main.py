from indeed import get_article_joongang
from hankyung import get_article_hankyung
from save import save_to_file

hankyung_arti = get_article_hankyung()
indeed_article = get_article_joongang()

total_arti = indeed_article + hankyung_arti 
save_to_file(total_arti)