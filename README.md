# CTF Sripts

Just a bunch of automation scripts or exploits I wrote while playing CTFs
Here mostly for re-usability (Yeah I am just that lazy).
you guessed those will be mostly in python buuut...

Some of those might be linked later to writeups (If I am not too lazy)
I write them on [zerOne](https://dev.nairolf32.com/zerOne) my cybersecurity blog.

## Usage

I could let you figure it yourself but hey...
clone the repo (obvioulsy) or just grab the script you want

### python scripts

I migrated to [uv](https://docs.astral.sh/uv) for python scripts which is recommended (evolution, people! evolution!) but you don't have to use it. uv handles most things alone but you might want to create your own `venv` if not using it and install the requirements listed at the top of almost each python script. Run the desired script with `python3 <script_name>.py` (or `uv run --script <script_name>.py` if you are civilized enough)

- scripts are named after the challenge I am solving
- scripts are placed in subfolders corresponding to the challenge platform
- if the script requires multiple files to work (crypto challs much) I add all that in a subfolder

Also note that all scripts here are WORKING! those were used by me to solve the challenges, BUT some refining might be needed. By example for challenges that use http requests, you might need to change the headers or the cookies or the data sent in the request, as for security reasons should be different for each user. Also, sometimes the challenge file might be missing so use yours and update the script. You are a hacker after all!

### bash scripts
c'mon do I really need to explain how to run a bash script? Just make sure to give it the right permissions with `chmod +x <script_name>.sh` and run it with `./<script_name>.sh` (or `bash <script_name>.sh`)

### JavaScript scripts

I don't have a lot of those but I use them for web challenges, you can run them in the browser console or with `node`. Just make sure to change the script if needed (like changing the url or something)

### Other scripts

I might have some low level scripts in other languages (like C, assembly or rust) so I obviously won't explain how to run all of them here. Just make sure to have the right environment and dependencies installed and run them with the appropriate command (like `go run <script_name>.go` or `cargo run <script_name>.rs`) with C and C++ scripts, you might need to compile them first with `gcc <script_name>.c -o <script_name>` or `g++ <script_name>.cpp -o <script_name>` and then run the compiled binary with `./<script_name>` You are a hacker after all.


## Disclaimer

HUGE SPOILER ALERT! If you are playing the same CTFs or solving the same challenges you should make sure to solve them yourself (or at least try A LOT) before looking at the scripts. I put these here mostly for myself (re-usability) and for educational purposes (others can compare their solutions to mine and vice versa). DO NOT RUIN THE FUN OR THE LEARNING EXPERIENCE! Also I am DEFINITELLY NOT RESPONSIBLE for any damage, loss or harm caused by using these scripts, use them at your own risk and always make sure to understand what they do before running them. stay ethical and responsible, and don't use them (somehow) for illegal activities.
