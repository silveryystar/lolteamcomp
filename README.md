# League of Legends Team Composition Tool
This tool helps the user analyze, find, and select ideal League of Legends team compositions.

# Setup
1. Install Python at https://www.python.org/downloads/.
2. Download repository.
3. Open Terminal in repository folder.
4. Enter ```pip install requests```.
5. Enter ```python main.py```.

# Usage
This program has three functions, *selector*, *analyzer*, and *finder*.
*selector* mimics Champion Select and prints current team composition.
*analyzer* returns information on specific champions.
*finder* recommends champions to select.

### Selector
To use *selector*, run *main.py* via ```python main.py``` in Terminal.
When ```Ban:``` prints, enter champions banned (non-case-sensitive).
To quit this loop, enter ```q```.
Bans are only necessary if using *finder* or *analyzer* to avoid finding or analyzing selected champions.

After, ```Champion:``` will print.
Enter champions selected (non-case-sensitive).
The values associated with the roles of each champion selected will sum and print.
A champion with a pure role has a value of 3 for that role.
For a champion with a primary and secondary role, the former has a value of 2, the latter 1.
After, ```['assassin', 'fighter', 'mage', 'marksman', 'support', 'tank']``` will print.
This list is the order in which the values printed.

To select opponents' champions, enter ```b``` when ```Champion:``` print.
After, ```Opponent champion``` will print.
Enter the champion the opponent selected (non-case-sensitive).
This is equivalent to a ban.
To quit the code, enter ```q```.

### Analyzer
*analyzer* is built into *selector*.
To use *analyzer*, follow the same steps as *selector* until ```Champion:``` prints.
Enter ```a```.
```Analysis champion:``` will print.
Enter the champion to analyze.

After, a list containing the roles of the entered champion will print.
If one role is printed, that role is the pure role of champion.
If two roles are printed, the first role printed is the primary role of the champion, the second the secondary.
After printing, the code will return to its original state in *selector*.

To quit *analyzer*, enter ```q``` when ```Analysis champion:``` prints.
Champions banned or selected cannot be analyzed.


### Finder
*finder* is built into *selector*.
To use *finder*, follow the same steps as *selector* until ```Champion:``` prints.
Enter ```f```.
```Primary role:``` will print.
Enter the pure, primary, or secondary role (non-case-sensitive).
After, ```Primary role value:``` will print.
Enter the value of the role.
For a pure role, enter ```3```.
For a primary role, enter ```2```.
For a secondary role, enter ```1```.

If ```3``` is entered, the program will print a list of champions with and only with that role.
If ```2``` or ```1``` is entered, the program will print ```Secondary role:```.
If the primary role was entered for ```Primary role:```, enter the secondary role.
If the secondary role was entered for ```Primary role:```, enter the primary role.
After, ```Secondary role value:``` will print.
If ```2``` was entered for ```Primary role value:```, enter ```1```.
If ```1``` was entered for ```Primary role value:```, enter ```2```.
A list will print of all champions with the specified primary and secondary role.
After printing, the code will return to its original state in *selector*. 

To quit *finder*, enter ```q``` when ```Primary role:```, ```Primary role value:```, ```Seondary role:```, or ```Secondary role value:``` prints.
Champions banned or selected cannot be found.

# Examples
### Selector
Arguably the simplest team composition in League of Legends consists of a toplane tank, a jungle fighter, a midlane mage/assassin, a botlane marksman, and a support support.
An example team composition would be **Shen** toplane, **Kayn** jungle, **Ahri** midlane, **Twitch** botlane, and **Lulu** support.
This team composition has role values of ```[3, 2, 3, 2, 2, 3]``` for ```['assassin', 'fighter', 'mage', 'marksman', 'support', 'tank']```.
Another example team composition would be **Ornn** toplane, **Lillia** jungle, **Akali** midlane, **Lucian** botlane, and **Nami** support.
This team composition has role values of ```[3, 3, 2, 3, 2, 2]``` for ```['assassin', 'fighter', 'mage', 'marksman', 'support', 'tank']```.

Suppose (unbeknownst to the user) the champions banned are **Garen**, **Warwick**, **Annie**, **Ashe**, **Blitzcrank**, **Irelia**, **Master Yi**, **Sylas**, **Jinx**, and **Yuumi**.
The champions blue side (the user's side) selects are **Shen**, **Kayn**, **Ahri**, **Twitch**, and **Lulu**.
The champions red side selects are **Ornn**, **Lillia**, **Akali**, **Lucian**, and **Nami**.

Run *main.py* via ```python main.py``` in Terminal.
Banned champions are known first.
When ```Ban:``` prints, enter **Garen**, **Warwick**, **Annie**, **Ashe**, **Blitzcrank**, **Irelia**, **Master Yi**, **Sylas**, **Jinx**, and **Yuumi**.
After entering all bans, enter ```q```.

Since the user is on blue side, the user's team select the first champion.
Suppose the blue side selects **Shen**.
When ```Champion:``` prints, enter ```Shen```.

After, red-side selects two champions.
Suppose red-side selects **Ornn** and **Lillia**.
When ```Champion:``` prints, enter ```b``` to "ban" red side's champions.
When ```Opponent champion:``` prints, enter ```Ornn```.
```Champion:``` will print again, enter ```b```, and ```Lillia``` when ```Opponent champion:``` prints.

Continue this process for all subsequent champions, namely **Kayn**, **Ahri**, **Twitch**, and **Lulu** for blue side, and **Akali**, **Lucian**, and **Nami** for red side.

Banning champions (either via ```Ban:``` or ```Opponent champion:```) is not necessary for the code to function.
However, to use **analyzer** and **finder** to their fullest extent, banning champions is necessary.

To quit the code, enter ```q```.

### Analyzer
Suppose the champion the user wants to analyze is **Ahri**.
Run *main.py* via ```python main.py``` in Terminal.
When ```Ban:``` prints, enter ```q```.
When ```Champion:``` prints, enter ```a```.

After, ```Analysis champion:``` will print.
Enter ```Ahri```.
**Ahri's** roles will print, namely ```['mage', 'assassin']```.
**Mage** is the primary role, and **assassin** is the secondary role.

After printing, the code will return to its original state in *selector*.
To quit the code, enter ```q```.

### Finder
Suppose the user wants to find a champion with primary role **mage** and secondary role **assassin**.
Run *main.py* via ```python main.py``` in Terminal.
When ```Ban:``` prints, enter ```q```.
When ```Champion:``` prints, enter ```f```.

After, ```Primary role: ``` will print.
Enter ```mage```.
When ```Primary role value:``` prints, enter ```2```.
After, ```Secondary role: ``` will print.
Enter ```assassin```.
When ```Secondary role value:``` prints, enter ```1```.

All champions with primary role **mage** and secondary role **assassin** will print, namely ```['malzahar', 'ahri', 'sylas']```.
**Malzahar**, **Ahri**, and **Sylas** have primary role **mage** and secondary role **assassin**.

After printing, the code will return to its original state in *selector*.
To quit the code, enter ```q```.

# Errors
1. ```Invalid input. Enter champion to ban or 'q' to quit.```
Solution: Enter champion or ```q```.
2. ```Invalid input. Enter champion to select, 'a' to analyze, 'f' to find, 'b' to ban, or 'q' to quit.```
Solution: Enter champion or ```a```, ```f```, ```b```, or ```q``` to analyze, find, ban, or quit, respectively.
3. ```Invalid input. Enter champion to analyze or 'q' to quit.```
Solution: Enter champion or ```q```.
4. ```Invalid input. Enter 'assassin', 'fighter', 'mage', 'marksman', 'support', or 'tank' for role, '1', '2', or '3' for role value, or 'q' to quit. Roles cannot be the same, and role values must sum to 3.```
Solution: For ```Role:``` enter a role, namely ```assassin```, ```fighter```, ```mage```, ```marksman```, ```support```, or ```tank```.
For ```Role value:``` enter ```3``` for pure role, ```2``` for primary role, and ```1``` for secondary role.
Role values can only be 1, 2, or 3, and must sum to 3 either via permutations of 1 and 2 or 3 alone.

A list of champions in League of Legends is found at https://www.leagueoflegends.com/en-us/champions/.

# Contact
For help, improvements, etc., feel free to contact **silveryystar** on Discord.
