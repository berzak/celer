import os
import argparse
import urllib.request


NEWS_DATASETS = {
            "PTB":   {"README": "README", 
                      "url": "https://catalog.ldc.upenn.edu/LDC95T7"},
            "BLLIP": {"README": "README.1st", 
                      "url": "https://catalog.ldc.upenn.edu/LDC2000T43"} 
            }
NEWS_READMES_DIR = "ptb_bllip_readmes"

def check_readme():
    codes = {"PTB": 0, "BLLIP": 0}
    for dataset in NEWS_DATASETS:
        try:
            codes[dataset] = os.stat(NEWS_READMES_DIR+"/"+dataset+"/"+NEWS_DATASETS[dataset]["README"]).st_size
        except OSError:
            print("Error:", dataset, NEWS_DATASETS[dataset]["README"], "file is missing.", 
            "Please download the dataset from", NEWS_DATASETS[dataset]['url'], "and copy this file to the", NEWS_READMES_DIR+'/'+dataset, "directory")
    return codes.values()

def obtain_data(url):
    try:
        urllib.request.urlretrieve(url)
        print("Done!")
    except IOError:
        print("Error: Failed obtaining the data from the specified url")

def main(release):
    codes = check_readme()
    if all(codes):
        print("Found README files for PTB-WSJ and BLLIP.")
        data_file = 'data_'+release+'.zip'
        url = "https://people.csail.mit.edu/berzak/"+str(sum(codes))+"/celer/"+data_file
        print("Downloading", data_file, "(this may take several minutes)...")
        obtain_data(url)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--release", "-r", type=str, choices=['v1.0', 'v2.0'], default='v1.0', help="Dataset release")
    args = parser.parse_args()
    main(args.release)