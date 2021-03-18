# Read the Data frm data source
# Save it in the data/raw for further process
import os
from  get_data import read_params, get_Data
import argparse

def load_save(config_path):
    config=read_params(config_path)
    df=get_Data(config_path)
    new_columns=[column.replace(" ","_") for column in df.columns]
    raw_data_path=config["load_data"]["raw_dataset_csv"]
    df.to_csv(raw_data_path,sep=",",index=False,header=new_columns)
    #print(new_columns)


if __name__ == '__main__':
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args=args.parse_args()
    load_save(config_path=parsed_args.config)