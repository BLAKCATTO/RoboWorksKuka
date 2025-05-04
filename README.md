## 🇵🇱 README – Animacja ramienia robota KUKA w RoboWorks

### Opis

Ten skrypt w języku Python generuje plik z danymi animacyjnymi do sterowania ramieniem robota KUKA w symulacyjnym środowisku **RoboWorks**. Kątowe wartości poszczególnych przegubów są obliczane z wykorzystaniem funkcji easingowych (wygładzających), co pozwala na realistyczną i płynną animację.

### Funkcjonalności

* Obsługa 6 przegubów (Theta1 – Theta6).
* Zdefiniowane zakresy ruchu i limity kątowe dla każdego przegubu.
* Różne funkcje wygładzania: `ease_in_out_sine`, `ease_in_out_quad`, `linear`.
* Eksport danych do pliku `.txt` w formacie zgodnym z RoboWorks (dane oddzielone spacją).

### Wymagania

* Python 3.x

### Użycie

1. Uruchom skrypt:

```bash
python3 kuka_PL.py
```

2. Plik wynikowy `kuka_animation.txt` zostanie zapisany w tym samym katalogu.
3. Załaduj plik w programie **RoboWorks** jako dane animacyjne.

### Struktura pliku wynikowego

Plik wynikowy zawiera 1500 kroków animacji, gdzie każda linia odpowiada jednej klatce czasowej i zawiera kąty 6 przegubów:

```
KukaTheta-1 KukaTheta-2 KukaTheta-3 KukaTheta-4 KukaTheta-5 KukaTheta-6
0.00        0.00        0.00        0.00        0.00        0.00
...
```

---

## 🇬🇧 README – KUKA Robot Arm Animation for RoboWorks

### Description

This Python script generates a motion data file to animate a KUKA robot arm within the **RoboWorks** simulation software. Joint angles are calculated using easing functions to create smooth and realistic movements.

### Features

* Supports 6 joints (Theta1 – Theta6).
* Defined motion sequences with time spans and angle ranges.
* Includes multiple easing options: `ease_in_out_sine`, `ease_in_out_quad`, `linear`.
* Exports data to a `.txt` file in RoboWorks-compatible format (space-delimited).

### Requirements

* Python 3.x

### Usage

1. Run the script:

```bash
python3 kuka_EN.py
```

2. The output file `kuka_animation.txt` will be created in the same directory.
3. Import the file into **RoboWorks** as motion data for your robot model.

### Output File Structure

The output file includes 1500 animation steps. Each line represents a single frame with the joint angles for all six axes:

```
KukaTheta-1 KukaTheta-2 KukaTheta-3 KukaTheta-4 KukaTheta-5 KukaTheta-6
0.00        0.00        0.00        0.00        0.00        0.00
...
```
