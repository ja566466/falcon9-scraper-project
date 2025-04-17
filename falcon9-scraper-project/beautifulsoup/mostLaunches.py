{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "4e727b0d-b06d-48d1-b109-7372fc613fca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Page fetched successfully.\n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "max() iterable argument is empty",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[11], line 48\u001b[0m\n\u001b[1;32m     45\u001b[0m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[1;32m     46\u001b[0m         \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFailed to fetch the page.\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m---> 48\u001b[0m extract_most_launches()\n",
      "Cell \u001b[0;32mIn[11], line 38\u001b[0m, in \u001b[0;36mextract_most_launches\u001b[0;34m()\u001b[0m\n\u001b[1;32m     35\u001b[0m                 boosters_data[serial_number] \u001b[38;5;241m+\u001b[39m\u001b[38;5;241m=\u001b[39m \u001b[38;5;241m1\u001b[39m\n\u001b[1;32m     37\u001b[0m \u001b[38;5;66;03m# Sort boosters by most launches\u001b[39;00m\n\u001b[0;32m---> 38\u001b[0m most_launches_booster \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mmax\u001b[39m(boosters_data, key\u001b[38;5;241m=\u001b[39mboosters_data\u001b[38;5;241m.\u001b[39mget)\n\u001b[1;32m     40\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28mopen\u001b[39m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mmostLaunches.txt\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mw\u001b[39m\u001b[38;5;124m'\u001b[39m) \u001b[38;5;28;01mas\u001b[39;00m file:\n\u001b[1;32m     41\u001b[0m     file\u001b[38;5;241m.\u001b[39mwrite(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mBooster with most launches: \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mmost_launches_booster\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m)\n",
      "\u001b[0;31mValueError\u001b[0m: max() iterable argument is empty"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "url = 'https://en.wikipedia.org/wiki/List_of_Falcon_9_first-stage_boosters'\n",
    "response = requests.get(url)\n",
    "\n",
    "def extract_most_launches():\n",
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
    "                        if serial_number not in boosters_data:\n",
    "                            boosters_data[serial_number] = 0\n",
    "\n",
    "                        boosters_data[serial_number] += 1\n",
    "\n",
    "        # Sort boosters by most launches\n",
    "        most_launches_booster = max(boosters_data, key=boosters_data.get)\n",
    "\n",
    "        with open('mostLaunches.txt', 'w') as file:\n",
    "            file.write(f\"Booster with most launches: {most_launches_booster}\\n\")\n",
    "            file.write(f\"Number of launches: {boosters_data[most_launches_booster]}\\n\")\n",
    "\n",
    "        print(\"mostLaunches.txt has been saved.\")\n",
    "    else:\n",
    "        print(\"Failed to fetch the page.\")\n",
    "\n",
    "extract_most_launches()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "61149197-44dc-40da-b970-2611d19a9b5e",
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
