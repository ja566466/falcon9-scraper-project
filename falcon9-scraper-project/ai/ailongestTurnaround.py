{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "1f3841d5-8e85-46f7-9d3e-3854b8500aff",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Page fetched successfully.\n",
      "longestTurnaround.txt has been saved.\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "from datetime import datetime\n",
    "\n",
    "# URL for Falcon 9 launch data\n",
    "url = 'https://en.wikipedia.org/wiki/List_of_Falcon_9_first-stage_boosters'\n",
    "response = requests.get(url)\n",
    "\n",
    "def parse_date(date_str):\n",
    "    date_formats = ['%d %B %Y', '%B %Y', '%Y-%m-%d', '%d-%m-%Y']\n",
    "    for date_format in date_formats:\n",
    "        try:\n",
    "            return datetime.strptime(date_str, date_format)\n",
    "        except ValueError:\n",
    "            continue\n",
    "    return None  # Return None if no valid date format is found\n",
    "\n",
    "def extract_longest_turnaround():\n",
    "    if response.status_code == 200:\n",
    "        print(\"Page fetched successfully.\")\n",
    "        soup = BeautifulSoup(response.content, 'html.parser')\n",
    "\n",
    "        launch_tables = soup.find_all('table', {'class': 'wikitable'})\n",
    "        boosters_data = {}\n",
    "\n",
    "        for table in launch_tables:\n",
    "            rows = table.find_all('tr')[1:]\n",
    "            for row in rows:\n",
    "                columns = row.find_all('td')\n",
    "\n",
    "                if len(columns) > 7:\n",
    "                    version = columns[1].text.strip()\n",
    "                    flight_number = columns[3].text.strip()\n",
    "                    launch_date = columns[2].text.strip()\n",
    "                    turnaround_time = columns[7].text.strip()\n",
    "\n",
    "                    if 'F9 B4' in version or 'F9 B5' in version:\n",
    "                        serial_number = columns[0].text.strip()\n",
    "\n",
    "                        # Skip rows with invalid or missing turnaround times\n",
    "                        if turnaround_time in ['—', 'No attempt', 'N/A']:\n",
    "                            print(f\"Skipping invalid turnaround time: {turnaround_time}\")\n",
    "                            continue\n",
    "\n",
    "                        # Parse launch date and store data\n",
    "                        launch_date_obj = parse_date(launch_date)\n",
    "                        if serial_number not in boosters_data:\n",
    "                            boosters_data[serial_number] = []\n",
    "\n",
    "                        boosters_data[serial_number].append({\n",
    "                            'flight_number': flight_number,\n",
    "                            'launch_date': launch_date_obj,\n",
    "                            'turnaround_time': turnaround_time\n",
    "                        })\n",
    "\n",
    "        # Write results to text file\n",
    "        with open('longestTurnaround.txt', 'w') as file:\n",
    "            file.write(\"Longest Turnaround Time:\\n\\n\")\n",
    "            for booster, launches in boosters_data.items():\n",
    "                file.write(f\"Booster {booster}:\\n\")\n",
    "                for launch in launches:\n",
    "                    file.write(f\"  Flight {launch['flight_number']} - Launch Date: {launch['launch_date']} - Turnaround Time: {launch['turnaround_time']}\\n\")\n",
    "\n",
    "        print(\"longestTurnaround.txt has been saved.\")\n",
    "    else:\n",
    "        print(\"Failed to fetch the page.\")\n",
    "\n",
    "extract_longest_turnaround()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a0054f1b-365f-4ee4-9ab1-9932a959bbee",
   "metadata": {},
   "outputs": [],
   "source": []
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
