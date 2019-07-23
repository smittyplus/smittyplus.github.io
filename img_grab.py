import requests
import json

with open('./_data/alumni.json') as fp:
    alumni = json.load(fp)
url = 'https://docs.google.com/uc?export=download'
for alum in alumni:
    if alum['recent_headshot'] and alum['name']:
        params = {'id': f'{alum["recent_headshot"].split("=")[1]}'}
        res = requests.get(url, params=params)
        with open(f'./images/headshots/{alum["name"].lower().replace(" ", "")}.jpg', 'wb') as fp:
            fp.write(res.content)


#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://content.googleapis.com/drive/v2beta/files/1gSpO7oYTt-RKg3N_gwJClJLcQXntfnKE?fields=alternateLink%2CcopyRequiresWriterPermission%2CcreatedDate%2Cdescription%2CfileSize%2CiconLink%2Cid%2Clabels(starred)%2ClastViewedByMeDate%2CmodifiedDate%2Cshared%2CteamDriveId%2CimageMediaMetadata(height%2C%20width)%2CthumbnailLink%2CuserPermission(id%2Cname%2CemailAddress%2Cdomain%2Crole%2CadditionalRoles%2CphotoLink%2Ctype%2CwithLink)%2Cpermissions(id%2Cname%2CemailAddress%2Cdomain%2Crole%2CadditionalRoles%2CphotoLink%2Ctype%2CwithLink)%2Cparents(id)%2Ccapabilities(canMoveTeamDriveItem%2CcanAddChildren%2CcanEdit%2CcanDownload%2CcanComment%2CcanRename%2CcanRemoveChildren%2CcanMoveItemIntoTeamDrive)%2Ckind&supportsTeamDrives=true&key=AIzaSyC1eQ1xj69IdTMeii5r7brs3R90eck-m7k', headers=headers)
