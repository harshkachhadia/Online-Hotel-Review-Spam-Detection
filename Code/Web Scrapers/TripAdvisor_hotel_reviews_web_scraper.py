# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 23:40:30 2020

@author: piyus
"""

import bs4
import urllib
import urllib.request as url
import pandas as pd

url_list=[
    
[
'https://www.tripadvisor.com/Hotel_Review-g45963-d91925-Reviews-ARIA_Resort_Casino-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d91925-Reviews-or5-ARIA_Resort_Casino-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d91925-Reviews-or10-ARIA_Resort_Casino-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d91925-Reviews-or15-ARIA_Resort_Casino-Las_Vegas_Nevada.html#REVIEWS'              ],

['https://www.tripadvisor.com/Hotel_Review-g45963-d91674-Reviews-Four_Seasons_Hotel_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d91674-Reviews-or5-Four_Seasons_Hotel_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d91674-Reviews-or10-Four_Seasons_Hotel_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d91674-Reviews-or15-Four_Seasons_Hotel_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS'    ],

['https://www.tripadvisor.com/Hotel_Review-g45963-d619205-Reviews-Skylofts_at_MGM_Grand-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d619205-Reviews-or5-Skylofts_at_MGM_Grand-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d619205-Reviews-or10-Skylofts_at_MGM_Grand-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d619205-Reviews-or15-Skylofts_at_MGM_Grand-Las_Vegas_Nevada.html#REVIEWS'          ],

['https://www.tripadvisor.com/Hotel_Review-g45963-d1123368-Reviews-Encore_At_Wynn_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d1123368-Reviews-or5-Encore_At_Wynn_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d1123368-Reviews-or10-Encore_At_Wynn_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d1123368-Reviews-or15-Encore_At_Wynn_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS'      ],

['https://www.tripadvisor.com/Hotel_Review-g45963-d503598-Reviews-Wynn_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS',
 'https://www.tripadvisor.com/Hotel_Review-g45963-d503598-Reviews-or5-Wynn_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS',
 'https://www.tripadvisor.com/Hotel_Review-g45963-d503598-Reviews-or10-Wynn_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS',
 'https://www.tripadvisor.com/Hotel_Review-g45963-d503598-Reviews-or15-Wynn_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS'                 ],

['https://www.tripadvisor.com/Hotel_Review-g45963-d97704-Reviews-The_Venetian_Resort-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d97704-Reviews-or5-The_Venetian_Resort-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d97704-Reviews-or10-The_Venetian_Resort-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d97704-Reviews-or15-The_Venetian_Resort-Las_Vegas_Nevada.html#REVIEWS'             ],


['https://www.tripadvisor.com/Hotel_Review-g45963-d1829539-Reviews-The_Cosmopolitan_of_Las_Vegas_Autograph_Collection-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d1829539-Reviews-or5-The_Cosmopolitan_of_Las_Vegas_Autograph_Collection-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d1829539-Reviews-or10-The_Cosmopolitan_of_Las_Vegas_Autograph_Collection-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d1829539-Reviews-or15-The_Cosmopolitan_of_Las_Vegas_Autograph_Collection-Las_Vegas_Nevada.html#REVIEWS'],

['https://www.tripadvisor.com/Hotel_Review-g45963-d91703-Reviews-Bellagio_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d91703-Reviews-or5-Bellagio_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d91703-Reviews-or10-Bellagio_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d91703-Reviews-or15-Bellagio_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS'                  ],

['https://www.tripadvisor.com/Hotel_Review-g45963-d2409054-Reviews-ARIA_Sky_Suites-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d2409054-Reviews-or5-ARIA_Sky_Suites-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d2409054-Reviews-or10-ARIA_Sky_Suites-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d2409054-Reviews-or15-ARIA_Sky_Suites-Las_Vegas_Nevada.html#REVIEWS'                   ],

['https://www.tripadvisor.com/Hotel_Review-g45963-d91762-Reviews-Caesars_Palace-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d91762-Reviews-or5-Caesars_Palace-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d91762-Reviews-or10-Caesars_Palace-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d91762-Reviews-or15-Caesars_Palace-Las_Vegas_Nevada.html#REVIEWS'                         ],

['https://www.tripadvisor.com/Hotel_Review-g45963-d15182489-Reviews-NoMad_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d15182489-Reviews-or5-NoMad_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d15182489-Reviews-or10-NoMad_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d15182489-Reviews-or15-NoMad_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS'                          ],

['https://www.tripadvisor.com/Hotel_Review-g45963-d596543-Reviews-Red_Rock_Casino_Resort_Spa-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d596543-Reviews-or5-Red_Rock_Casino_Resort_Spa-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d596543-Reviews-or10-Red_Rock_Casino_Resort_Spa-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d596543-Reviews-or15-Red_Rock_Casino_Resort_Spa-Las_Vegas_Nevada.html#REVIEWS'                 ],


['https://www.tripadvisor.com/Hotel_Review-g45963-d1474086-Reviews-Vdara_Hotel_Spa_at_ARIA_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d1474086-Reviews-or5-Vdara_Hotel_Spa_at_ARIA_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d1474086-Reviews-or10-Vdara_Hotel_Spa_at_ARIA_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d1474086-Reviews-or15-Vdara_Hotel_Spa_at_ARIA_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS'         ],

['https://www.tripadvisor.com/Hotel_Review-g45963-d1022061-Reviews-Trump_International_Hotel_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d1022061-Reviews-or5-Trump_International_Hotel_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d1022061-Reviews-or10-Trump_International_Hotel_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d1022061-Reviews-or15-Trump_International_Hotel_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS'       ],

['https://www.tripadvisor.com/Hotel_Review-g45953-d1235866-Reviews-M_Resort_Spa_Casino-Henderson_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45953-d1235866-Reviews-or5-M_Resort_Spa_Casino-Henderson_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45953-d1235866-Reviews-or10-M_Resort_Spa_Casino-Henderson_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45953-d1235866-Reviews-or15-M_Resort_Spa_Casino-Henderson_Nevada.html#REVIEWS'                       ],

['https://www.tripadvisor.com/Hotel_Review-g45963-d91886-Reviews-Mandalay_Bay_Resort_Casino-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d91886-Reviews-or5-Mandalay_Bay_Resort_Casino-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d91886-Reviews-or10-Mandalay_Bay_Resort_Casino-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d91886-Reviews-or15-Mandalay_Bay_Resort_Casino-Las_Vegas_Nevada.html#REVIEWS'                  ],

['https://www.tripadvisor.com/Hotel_Review-g45963-d1456410-Reviews-Waldorf_Astoria_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d1456410-Reviews-or5-Waldorf_Astoria_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d1456410-Reviews-or10-Waldorf_Astoria_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d1456410-Reviews-or15-Waldorf_Astoria_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS'                 ],

['https://www.tripadvisor.com/Hotel_Review-g45963-d496876-Reviews-Delano_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d496876-Reviews-or5-Delano_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d496876-Reviews-or10-Delano_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d496876-Reviews-or15-Delano_Las_Vegas-Las_Vegas_Nevada.html#REVIEWS'                       ],

['https://www.tripadvisor.com/Hotel_Review-g45963-d3907285-Reviews-Nobu_Hotel_at_Caesars_Palace-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d3907285-Reviews-or5-Nobu_Hotel_at_Caesars_Palace-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d3907285-Reviews-or10-Nobu_Hotel_at_Caesars_Palace-Las_Vegas_Nevada.html#REVIEWS',
'https://www.tripadvisor.com/Hotel_Review-g45963-d3907285-Reviews-or15-Nobu_Hotel_at_Caesars_Palace-Las_Vegas_Nevada.html#REVIEWS']

]


def ExtractReviews(urllist):

  reviews=[]

  for h in range(len(urllist)):

    opener = url.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    
    srclink_hotel = opener.open(urllist[h])
    data_hotel = bs4.BeautifulSoup(srclink_hotel,'html.parser')

    hotel_name = data_hotel.find("h1", {"class": "_1mTlpMC3"}).string

    review_raw = data_hotel.find_all("q", {"class":"IRsGHoPm"})

    for i in range(len(review_raw)):
      reviews.append(review_raw[i].get_text())

  reviews = list(dict.fromkeys(reviews))
  print("")

  return [['TripAdvisor']*len(reviews), [hotel_name]*len(reviews), reviews]

final_reviews_list = []
final_hotel_name_list = []
final_source_list = []

for l in range(len(url_list)):
  current_url_list = url_list[l]
  output = ExtractReviews(current_url_list)

  final_reviews_list.append(output[2])
  final_hotel_name_list.append(output[1])
  final_source_list.append(output[0]) 

for i in range(len(final_reviews_list)):
  if len(final_reviews_list[i])>=20:
    final_reviews_list[i] = final_reviews_list[i][:20]
    final_hotel_name_list[i] = final_hotel_name_list[i][:20]
    final_source_list[i] = final_source_list[i][:20]

merged_hotel_list = []
merged_reviews_list = []
merged_source_list = []

for sub in final_hotel_name_list:
  for item in sub:
    merged_hotel_list.append(item)

for sub in final_reviews_list:
  for item in sub:
    merged_reviews_list.append(item)

for sub in final_source_list:
  for item in sub:
    merged_source_list.append(item)   

final_df = pd.DataFrame(list(zip(merged_hotel_list, merged_source_list, merged_reviews_list)),columns =['Hotel', 'Source', 'Text'])
final_df.to_csv("TripAdvisor_hotel_reviews.csv",index=False)