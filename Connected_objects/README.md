# Connected objects 

## 📌 Table of Contents :

I. [Presentation](#📋-presentation)

II. [Equipment required](#⚙️-system-architecture)

III. [3D models](#💻-installation) 

IV. [Schématic](#💻-installation) 

V. [Installation and Assembly](#💻-installation) 

## 📋 Presentation :
Currently, Domolabo includes one connected device: a mini fan. <br>This mini fan can be controlled via the central hub and the mobile application, allowing users to adjust the fan's activation and speed.

## ⚙️ Equipment required :

- [ESP32](https://www.amazon.fr/JZK-développement-dantenne-Bluetooth-Batterie/dp/B071JR9WS9/ref=sr_1_9?__mk_fr_FR=ÅMÅŽÕÑ&crid=1X1GUMHSZ09LX&dib=eyJ2IjoiMSJ9.WCOjNJnOCaxWwqfJwnFlpMRPewvZIcY9yC1zzaI-mHULyqTkyY8NYd-RHyxFs0ZpJ4StpwOYnI6J48T5egHuN7dMJzEHUjAnu3_TM6V-RFiWM-flO1Ww2CmPMuF5cmlzjhGMHJdSbLLsQl3ID1RyDXTK1kyW1npQ6Fdd3guuEiQTj5VvxQdNis0zRmq4FH326MGpgX6uBZbXntSyc6S8qRQiTPqRIYVQwFVvU_-io4pKK4zkg2Hqc1KshjZ3QGFGRbhLKL16pPv6cZEMp9myWNQZ9kDOzfaobDsBHjkB6Ik.bYSpHdQrGKugm5NCQ1VcycZmsR8E52ZnZTF957Du3rs&dib_tag=se&keywords=esp32&qid=1716073219&sprefix=iesp32%2Caps%2C85&sr=8-9)
- [Motor DC](https://www.amazon.fr/DC3V-12V-Moteur-Voiture-Motrices-robotique/dp/B0BDQMV4CQ/ref=sr_1_24?__mk_fr_FR=ÅMÅŽÕÑ&crid=20LJI8Q2FK21&dib=eyJ2IjoiMSJ9.N8Ez_hZfz_66Fol_BUQUtx7siIgU9V3QkBdKuo2TNkszv-LfCsP2cUMKy8WfCI-9Ex-VyQRr7MjPc5X0HtzqYRksdrv-uW9kd7HU639Y4tZ9W0oHcKBc6UG4hoTPQD_p-Fpa9HnutQOaIT45tne9b9K-Gvy3LRFblOG6nLHXNY6oLoDbj1uFfJGwoJD8ljKGB119sp2_2VKSGeNEt-w6mVe1Vb-KDHjQ73I8VSorun88eUo8BP2H1YaMavixAe8xyZf5_LOD-3P_q8MMRdPfjie7VazwPwpW1N1MZZ_FQ40.FO5AQg7RG37DeVHIwe4jbKL4t03UPgETi3Q01VQwdSQ&dib_tag=se&keywords=moteur+dc&qid=1716073391&sprefix=moteur+dc%2Caps%2C87&sr=8-24)
- [Switch](https://www.amazon.fr/Gebildet-Interrupteur-Commutateur-Micro-Interrupteur-Verrouillage/dp/B07Z4RW9X6/ref=sr_1_8?__mk_fr_FR=ÅMÅŽÕÑ&crid=QUICSRBQG738&dib=eyJ2IjoiMSJ9.ZCMKzsk5YAezroeS-NcRE18PtreoyPJ2oWltL11MIbhiSKqZEdEf9-Enn1jINVg9YIeH8LH2Jp9kvIhiml4f-sqq0MztFOqtsPQs10O_stLesobpvuEcxvT6wyt47mHOHvTcWHirArPOXmhA9BrjU4tP8bppv-bHLQ0wKqqZ4HGtWZq2XGxaUoWNFKYG-DHaBIdsgPAsROSpSXb2MAKXsWHgVgVa0_dGp6avvUyDG3Wy40bFYA7bM1xKN8eAakb2Eb8AxsUoUANQYCMwLsm4UephzdxOWPuwxoaPPA1b3-I.Pw0FZbqCqwwNPmGGJEYae8u3EmNv_f_qoaf66sN4aEg&dib_tag=se&keywords=commutateur+a+glissiere&qid=1716073560&sprefix=commutateur+a+glissiere%2Caps%2C93&sr=8-8)
- [Button](https://www.amazon.fr/Interrupteurs-Bouton-poussoir-Assortiment-dInterrupteurs-Interrupteur/dp/B0B8ZRVJG8/ref=sr_1_5?__mk_fr_FR=ÅMÅŽÕÑ&crid=11O8YDFMRGST1&dib=eyJ2IjoiMSJ9.ZuIDdmcPFvanlbT63Vz0uvL73ja91pZJarmmypFuHU5TO_TlQg35Pw-BJUddlZeSLsRM_x6vmAYEv4o4brT8kGq_zfQRCiH58SbpoApUN1ElnbN5aPqEo1vVeoeYaVQiB8-P3MOt4QDzooPhRYG7kR27JWnXf0bPBi56SibMR6ODYRa17GIU9dPkd1zeE74BPlaz7muFxJKK4o1anxzPI9ZEvrPPWC8XGweoXCFsyLzDpaVFwc9fGaa_mniHm5FNfcMHCUud1HZwmf0268x8KCPG08oN6Bu96EQnkILGkcc.wjIha-V4B1Kv8Ge7EDVnbL4SWNiP12BF8ljh5HknbRY&dib_tag=se&keywords=switch+button&qid=1716073461&sprefix=switch+button%2Caps%2C86&sr=8-5)
- [MX1616](https://www.amazon.ca/-/fr/CANADUINO®-pilotes-moteur-MX1616-TC1508A/dp/B09TYBRQZG)
- [Dupond cable](https://www.amazon.fr/Elegoo-Breadboard-Femelle-Longueur-Arduino/dp/B01JD5WCG2/ref=sr_1_5?__mk_fr_FR=ÅMÅŽÕÑ&crid=2I5PL2B2K5BZK&dib=eyJ2IjoiMSJ9.s8dXeZGC6G2PoYh3lqEXHoU5G5__ot-EnLbx2sdQ4fJnHfvU-BVziZ5dSkoNiNLUF49szgm65TUx5ntTvJm5EJm4YmjGMCAc0HsIULwZ9s3lR-7-rWQd7cOp8msCCWuzKxMAe-zYM_OwPxfoQj43-EFYTQHFRn1tr_WqlM4HF-HhdYQrhLvIy9a5fLdI1vr-Wkuz_x9EcY5qUbvgEbZ0gn6KDq6VD7ksk4xVOVsIuxcN2u12heyeeGU7QkEzd-lkv8Ch6wJ76dtP_luTy87yF2XIHU3ThybNnUNSLtM4p5s.Mal-073-PNfRlcYeuivU0Bp8Tgy4itWI9j7Vl6_MAtM&dib_tag=se&keywords=cable+dupont&qid=1716073582&sprefix=cable+dupond%2Caps%2C83&sr=8-5)
- [Battery connector](https://www.amazon.fr/HeyNana-supports-connecteur-clip-batterie/dp/B0919H1113/ref=sr_1_5?__mk_fr_FR=ÅMÅŽÕÑ&crid=1MJN6O1J52P9M&dib=eyJ2IjoiMSJ9.nRoejk_aQ1wS6k86fwrebdqybadZC3zhLxF9J-CSDFNU7b6601s86FWNe0dHd93EV5S6RzOmwCx5qpc-07UnMl7Y-8u0gCCFIlVXSRyDRs0T__CimoCvV2S0ccCo5Gndq3A-sBRK6KU2XRYr4fY9lHmcVmTDykfDmyOUiZjE_L4HBDoV50l9xNqc9QHcdugqfQdeFp5AxwOUa30sDF288_WgS2F0dmlR5Kil125jeWY8QOBQMMrM5gzydG_NiSV9YcSeAqjpP5Z1fgzpEeL8m8lN9rBMqo4gZ3ljFzoqo80.WvNV6-wmPce8uC61odjh-aqh9G_GzqbqpsV3m15VjRQ&dib_tag=se&keywords=connecteur+pile+9v&qid=1716073594&sprefix=connecteur+pile+9v%2Caps%2C84&sr=8-5)
- [9V battery](https://www.amazon.fr/HeyNana-supports-connecteur-clip-batterie/dp/B0919H1113/ref=sr_1_5?__mk_fr_FR=ÅMÅŽÕÑ&crid=1MJN6O1J52P9M&dib=eyJ2IjoiMSJ9.nRoejk_aQ1wS6k86fwrebdqybadZC3zhLxF9J-CSDFNU7b6601s86FWNe0dHd93EV5S6RzOmwCx5qpc-07UnMl7Y-8u0gCCFIlVXSRyDRs0T__CimoCvV2S0ccCo5Gndq3A-sBRK6KU2XRYr4fY9lHmcVmTDykfDmyOUiZjE_L4HBDoV50l9xNqc9QHcdugqfQdeFp5AxwOUa30sDF288_WgS2F0dmlR5Kil125jeWY8QOBQMMrM5gzydG_NiSV9YcSeAqjpP5Z1fgzpEeL8m8lN9rBMqo4gZ3ljFzoqo80.WvNV6-wmPce8uC61odjh-aqh9G_GzqbqpsV3m15VjRQ&dib_tag=se&keywords=connecteur+pile+9v&qid=1716073594&sprefix=connecteur+pile+9v%2Caps%2C84&sr=8-5)
- [DCDC converter](https://www.amazon.fr/Convertisseur-Abaisseur-Converter-Alimentation-Réglable/dp/B08LVZL61S/ref=sr_1_5?__mk_fr_FR=ÅMÅŽÕÑ&crid=12W5JBOAQTPK4&dib=eyJ2IjoiMSJ9.8bF51y6CAAg_VSy7tL93ioOBOYPjKCL4FS2SRJp2u1wbcS7hJ5TwUZZAyTAdbbcSF6NpukObWqjhS388W8i6F7bEebivonnDNKZwKKlm4iOtdfUkhpQrGWUv6KF4p2m5ikAeICp87T48OCNDDYp7P2yRT2q2nJUs-P8jIQ5SgyO4BIjWRo7X8KC8OGDo4JJNxqKuOOtuwd9jf5wcaTUr9tJ7udG0gYsmtnqsaqo14p_gTbwjNJnStLkd-7lnXWXfeXOzWy2zw8z1xYTwGQ5pCwfFIi1MOkb2TaPlJeexZKQ.BreVJ3JgcmmgHj86IsYK93htNY6FpmgiXn7eKwrmB8c&dib_tag=se&keywords=convertisseur+dc+dc&qid=1716073627&sprefix=convertisseur+dcdc%2Caps%2C86&sr=8-5)
- [Magnet](https://www.amazon.fr/Sapphome-Réfrigérateur-Puissants-Métalliques-Calendrier/dp/B0BX3VVFGX/ref=sr_1_5?__mk_fr_FR=ÅMÅŽÕÑ&crid=1UWO0NDX9DQUU&dib=eyJ2IjoiMSJ9.-EWQbQsLevx-drI38-admkr7h1PAkuhLQKzTs-ESwqI8jjQ7G98SV-OkM_WeH9UeO9bVMCtqM9vFUQugWLEVL8Y8B9WpuuLZIXtGuFxJDwXwh-9zeb7q55ko985IYoF1HPd_lLI60c7qi4f3CyPnnWWVveryM9IaCr3kOrGaUx8AfriKsheWcIYzdUam4Q2hPt9a2iRLH0L7bpyfYPCDFabyHFvU8OEZHl4fUp1TUc7qeqcP3HCgcnl-E6w0zbd16Oh_pAU3EZdIz3ElGpDa8ribd_wUvW9ItYQaIK96QMU.omjoh481TssyGKypHPEB7zUpWP4B6c2BIp65aUnd864&dib_tag=se&keywords=aimants&qid=1716073865&sprefix=aimants%2Caps%2C82&sr=8-5)

## 🔰 3D models :
you can view the current model here : https://a360.co/3UFd5A0

The entire object can be printed in 3d from the files present in this folder :

[3D Models](/Connected_objects/Fan/3D_models/)

## 💡 Schématic :

You can find the electrical schematics in the [schematics folder](/Connected_objects/Fan/SCH/)

## 💻 Installation :

1. Put the code on the Esp32 (you can use [rshell](https://micropython.fr/05.outils/terminal_serie/rshell/))

2. Carry out the electronic assembly following the [schematic](/Connected_objects/Fan/SCH/) 

3. Put it in the printed model

4. Turn on the switch

5. Enjoy !😉
