
int rel1 = 4; // дигитал порт для первой реле
int rel2 = 3; // дигитал порт для второй реле
int klapon = 8; // дигитал порт для силового ключа, к которому подключен клапан
int update_interval=100; // интервал в мс 
unsigned long last_time=0; // время последнего обновления данных с блютуз
char data_in; // переменная хранящая в себе информацию с приложения блютуз
unsigned long vnosed_time;
int slider_value;
int motor_speed = A1;


void setup() {
  pinMode(rel1, OUTPUT);// пинмод для 4-го 
  pinMode(rel2, OUTPUT);// пинмод для 3-го
  pinMode(motor_speed, OUTPUT);
  pinMode(klapon, OUTPUT);// пинмод для 8-го
  Serial.begin(9600); // обмен данными соскоростью 9600
}
void rightRelforward(){ // создание функции, которая хранит в себе состояние пинов 4,3
  digitalWrite(rel2,LOW);
  digitalWrite(rel1,HIGH);

}
void leftRelback(){ // создание функции, которая хранит в себе состояние пинов 4,3
  digitalWrite(rel1,LOW);
  digitalWrite(rel2,HIGH);

}
void relstop(){ // создание функции, которая хранит в себе состояние пинов 4,3
  digitalWrite(rel1,LOW);
  digitalWrite(rel2,LOW);
}
void loop() { 
  if(millis()-vnosed_time<=200){// открытие и закрытие клапана на 8 пине
    vnosed_time = millis()+ 5000;
    Serial.println("KlaponON");
    digitalWrite(klapon, HIGH);
  }
  else{
    Serial.println("KlaponOFF");
    digitalWrite(klapon, LOW);
  }
  if (Serial.available()){
    data_in=Serial.read();  // внос данных с телефона в переменную data_in
    if (data_in == 'A'){
      slider_value = Serial.parseInt();
      Serial.println(slider_value);
      slider_value = motor_speed;
    }

    if(data_in=='F'){ // движение вперёд
      rightRelforward(); // вызов функции 
    }

    if(data_in=='B'){ // движение назад
      leftRelback(); // вызов функции
    }
    if(data_in=='S'){ // выключение двух реле
      relstop(); // вызов функции
    }
}


  ///////////// Отправление данных на телефон

  unsigned long t=millis();
  if ((t-last_time)>update_interval){
    last_time=t;

  }

}

