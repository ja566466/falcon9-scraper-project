{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "126bd844-e3a6-4db6-a610-24b272b1b5b2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Page fetched successfully. Status Code: 200\n",
      "f9only.txt has been saved.\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "# URL for Falcon 9 launch data\n",
    "url = 'https://en.wikipedia.org/wiki/List_of_Falcon_9_first-stage_boosters'\n",
    "response = requests.get(url)\n",
    "print(f\"Page fetched successfully. Status Code: {response.status_code}\")\n",
    "\n",
    "# Parse the HTML content\n",
    "soup = BeautifulSoup(response.text, 'html.parser')\n",
    "\n",
    "# Find all tables with class 'wikitable'\n",
    "launch_tables = soup.find_all('table', {'class': 'wikitable'})\n",
    "\n",
    "# List to hold the launch data for f9only\n",
    "f9only_data = []\n",
    "\n",
    "# Iterate through tables to find relevant data\n",
    "for table in launch_tables:\n",
    "    rows = table.find_all('tr')[1:]  # Skip header row\n",
    "    for row in rows:\n",
    "        columns = row.find_all('td')\n",
    "        if len(columns) > 7:\n",
    "            version = columns[1].text.strip()\n",
    "            if 'F9' in version:  # Only capture Falcon 9 data\n",
    "                serial_number = columns[0].text.strip()\n",
    "                launch_date = columns[2].text.strip()\n",
    "                flight_no = columns[3].text.strip()\n",
    "                payload = columns[4].text.strip()\n",
    "                launch_pad = columns[5].text.strip()\n",
    "                landing_location = columns[6].text.strip()\n",
    "                fate = columns[7].text.strip()\n",
    "                turnaround_time = columns[8].text.strip() if len(columns) > 8 else 'N/A'\n",
    "\n",
    "                # Add the captured data to the list\n",
    "                f9only_data.append({\n",
    "                    'Serial Number': serial_number,\n",
    "                    'Version': version,\n",
    "                    'Launch Date': launch_date,\n",
    "                    'Flight Number': flight_no,\n",
    "                    'Payload': payload,\n",
    "                    'Launch Pad': launch_pad,\n",
    "                    'Landing Location': landing_location,\n",
    "                    'Fate': fate,\n",
    "                    'Turnaround Time': turnaround_time,\n",
    "                })\n",
    "\n",
    "# Save the extracted data to a text file (f9only.txt)\n",
    "if f9only_data:\n",
    "    with open('f9only.txt', 'w') as file:\n",
    "        for entry in f9only_data:\n",
    "            file.write(str(entry) + '\\n')\n",
    "    print(\"f9only.txt has been saved.\")\n",
    "else:\n",
    "    print(\"No data to save for f9only.txt.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "52c0fb57-5eec-4797-95ef-45974d7c3d60",
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
