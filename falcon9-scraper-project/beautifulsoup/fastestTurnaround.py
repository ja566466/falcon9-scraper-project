{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "03e4d447-75fb-462d-b284-25eba45d50d4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Page fetched successfully.\n",
      "fastestTurnaround.txt has been saved.\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "from datetime import datetime\n",
    "\n",
    "url = 'https://en.wikipedia.org/wiki/List_of_Falcon_9_first-stage_boosters'\n",
    "response = requests.get(url)\n",
    "\n",
    "def extract_fastest_turnaround():\n",
    "    if response.status_code == 200:\n",
    "        print(\"Page fetched successfully.\")\n",
    "        soup = BeautifulSoup(response.content, 'html.parser')\n",
    "\n",
    "        launch_tables = soup.find_all('table', {'class': 'wikitable'})\n",
    "\n",
    "        boosters_data = {}\n",
    "\n",
    "        for table in launch_tables:\n",
    "            rows = table.find_all('tr')[1:]  # Skip header row\n",
    "            for row in rows:\n",
    "                columns = row.find_all('td')\n",
    "\n",
    "                if len(columns) > 7:\n",
    "                    version = columns[1].text.strip()\n",
    "                    if 'F9 B4' in version or 'F9 B5' in version:\n",
    "                        serial_number = columns[0].text.strip()\n",
    "                        flight_number = columns[3].text.strip()\n",
    "                        launch_date = columns[2].text.strip()\n",
    "\n",
    "                        # Skip invalid dates\n",
    "                        if launch_date in ['—', 'N/A', 'No attempt']:\n",
    "                            continue\n",
    "\n",
    "                        try:\n",
    "                            launch_date_obj = datetime.strptime(launch_date, '%d %B %Y')\n",
    "                        except ValueError:\n",
    "                            continue\n",
    "\n",
    "                        if serial_number not in boosters_data:\n",
    "                            boosters_data[serial_number] = []\n",
    "\n",
    "                        boosters_data[serial_number].append({\n",
    "                            'flight_number': flight_number,\n",
    "                            'launch_date': launch_date_obj\n",
    "                        })\n",
    "\n",
    "        # Calculate turnaround times and save to file\n",
    "        with open('fastestTurnaround.txt', 'w') as file:\n",
    "            file.write(\"Fastest Turnaround Calculations:\\n\\n\")\n",
    "            for booster, launches in boosters_data.items():\n",
    "                if len(launches) > 1:\n",
    "                    launches.sort(key=lambda x: x['launch_date'])\n",
    "\n",
    "                    for i in range(1, len(launches)):\n",
    "                        turnaround_time = (launches[i]['launch_date'] - launches[i - 1]['launch_date']).days\n",
    "                        file.write(f\"Turnaround time between Flight {launches[i-1]['flight_number']} and {launches[i]['flight_number']}: {turnaround_time} days\\n\")\n",
    "\n",
    "        print(\"fastestTurnaround.txt has been saved.\")\n",
    "    else:\n",
    "        print(\"Failed to fetch the page.\")\n",
    "\n",
    "extract_fastest_turnaround()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
