const int buttonPin  = 2;

const int greenPin = 10;
const int redPin = 8;
const int bluePin = 9;

int buttonState = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(buttonPin, INPUT);
  
  Serial.begin(9600);
  
  pinMode(greenPin, OUTPUT);
  pinMode(redPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}

void loop() {
  
  // put your main code here, to run repeatedly:
  buttonState = digitalRead(buttonPin);

  if (buttonState == LOW) {
    Serial.println("Take a picture!");
      while (buttonState == LOW) {
        // Wait
        buttonState = digitalRead(buttonPin);
    }
  }

  int result = Serial.read();
 
  if (result == 1) {
    setColor(0, 255, 0);
    delay(10000);
  }
  else if (result == 0) {
    setColor(255, 0, 0);
    delay(10000);
  } 
  else {
    setColor(0, 0, 0);
  }
  
}

void setColor(int red, int green, int blue) {
  #ifdef COMMON_ANODE
    red = 255 - red;
    green = 255 - green;
    blue = 255 - blue;

  #endif

  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue);
    
}
