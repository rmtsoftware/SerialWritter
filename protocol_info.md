
--- 
# Общение с NavBoard НАЧАЛО
Данные передаются в виде ASCII строк.
Каждая строка начинается с 2 байт признака сообщения: <0x44> <0x73>
Каждая строка заканчивается символами перевода каретки и возврата строки <0x0D><0x0A>
Блоки данных разделяются запятыми.
Скорость обмена: 115200

### Формат посылки данных:
`<0x44>,<0x73>,<Адрес устройства>,<ID сообщения>,<Данные>,....,<Данные>,<CRC>,<0x0D><0x0A>`

##### <ID сообщения>:

- 1 - Данные GPS (Latitude,NS,Longitude,EW,Altitude,Time,speed_kmph,RMC_course)

- 2 - Данные датчиков (AXL_x,AXL_y,AXL_z,MAG_x,MAG_y,MAG_z,GYRO_x,GYRO_y,GYRO_z,Gnd_Heading,) 

##### Пример 1 "Данные GPS": 
Запрос GPS:  		`D,s,1,1,*95\r\n`

Ответ от NavBoard: `D,s,1,1,5430.1270,N,1920.2310,E,15.2,081121,38.000,48.000,*76`

Расшифровка:  		
`D,s,<адрес>,<ID сообщения>,<Latitude>,<NS>,<Longitude>,<EW>,<Altitude>,<Time UTC>,<speed_kmph>,<RMC_course>,<CRC><\r><\n>`

##### Пример 2 "Данные IMU":  
Запрос IMU:  		`D,s,1,2,*92\r\n`

Ответ от NavBoard:  `D,s,1,2,29991,19308,27712,3152,3457,30389,3007,17862,2765,127.750,*69`

Расшифровка:  		`D,s,<адрес>,<ID сообщения>,<AXL_x>,<AXL_y>,<AXL_z>,<MAG_x>,<MAG_y>,<MAG_z>,<GYRO_x>,<GYRO_y>,<GYRO_z>,<Gnd_Heading_INS>,<CRC><\r><\n>`

---
# Общение с NavBoard-OrangePi

- Команды управления для руления АНПА от OrangePI: 
	`D,s,4,F,100,*\r\n`  - см. выше.
	Ответ на принятую команду в OrangePI: `D,s,3,*CRC\r\n`


- Прием данных OrangePI - "Пульт дистанционного управления"
	`D,s,5,RC,*\r\n`
	Ответ на принятую команду в OrangePI: `D,s,5,*CRC\r\n`

- Команда START ДВС: `D,s,ESTART,*\r\n` 
	Ответ от МB `D,s,ESTART,*CRC\r\n`

- Команда STOP ДВС:  `D,s,ESTOP,*CRC\r\n`
	Ответ от МB `D,s,ESTOP,*CRC\r\n`

- Команда запросить координаты АНПА с NavBoard: `D,s,4,GPS,*\r\n`


---
#### Функция для вычисления контрольной суммы строки NavBoard
```
unsigned char calculateChecksum(const char *sentence) {
    unsigned char checksum = 0;
    int i;
    // Пропускаем начальный символы 'D','s' и идем до символа '*'
    for (i = 2; sentence[i] != '*'; i++) {
        checksum ^= sentence[i];
    }
    return checksum;
}
```

---

`D,s,1,2,546,21068,15139,11540,4355,8600,28862,20656,15206,168.000,*65\r\n` - IMU

`D,s,1,1,5430.0972,N,1920.1740,E,15.2,132653,38.000,48.000,*77\r\n` - GPS

`D,s,1,1,*95\r\n` - GPS

`D,s,1,2,*92\r\n` - IMU

