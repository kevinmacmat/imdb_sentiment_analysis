def cleanText(data_frame, column_name:str, new_column:str):
	data_frame[column_name] = data_frame[column_name].str.replace('<br />', ' ')
	data_frame[new_column] = data_frame[column_name]
	data_frame[new_column] = data_frame[new_column].str.replace("'", '')    
	data_frame[new_column] = data_frame[new_column].str.replace('[^\w\s]', ' ')
	data_frame[new_column] = data_frame[new_column].str.replace('[0-9]', ' ')
	data_frame[new_column] = data_frame[new_column].str.replace('_', ' ')
	data_frame[new_column] = data_frame[new_column].str.replace('\s+', ' ')
	data_frame[new_column] = data_frame[new_column].str.lower()






# def getFileNamesList(directory:str):
#     # Need to import os for function to work
#     file_names = []

#     for filename in os.listdir(directory):
#         if filename.endswith(".txt"):
#             file_names.append(filename)
#             continue
#         else:
#             continue
            
#     return file_names


# def textToSeries(file_path:str, files_list:list):
#     # Create an empty pandas Series
#     reviews_series = pd.Series()
#     # For each file in files_list
#     for file_name in files_list:
#         # Access the text with file path and file name 
#         with open(file_path + file_name) as f:
#             # Read the text in as a Series and append it to reviews_series
#             reviews_series.append(pd.Series(f.readlines()))
#     # Return the reviews series         
#     return reviews_series     
