# realway

Show daily highway info, price.

Release History

- V0.1.0

  - 20220726
    - add toml config file(10 cities)
    - use requests get data
    - save data to json file
    - pytest verify city name euqal to pinyin

  - 20220727
    - setup gitee repo, deploy daily auto obtaion api data.
    - add pytest : combination city nums.

  - 0802
    - update export_json_data to date folder.
    - add pytest data path and data folder.

  - 0807
    - add function export to mongodb

#TODO

- [ ] multi thread get api data.
- [ ] 设置 http 自动跳转为 https
