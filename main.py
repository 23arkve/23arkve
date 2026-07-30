import os
from datetime import datetime
from zoneinfo import ZoneInfo
from dotenv import load_dotenv
import gifos

load_dotenv()

# explicitly ensure catppuccin mocha theme is active
os.environ["GIFOS_GENERAL_COLOR_SCHEME"] = "catppuccin-mocha"
os.environ["GIFOS_GENERAL_DEBUG"] = "false"

FONT_MAIN = "./JetBrainsMonoNL-Bold.ttf"
FONT_LOGO = "./VTKS BLOCKETO.ttf"

def main():
    # initialize terminal object with catppuccin mocha theme & jetbrainsmono font (line_spacing=0 for 1:1 square cat blocks)
    t = gifos.Terminal(
        width=750,
        height=520,
        xpad=15,
        ypad=15,
        font_file=FONT_MAIN,
        font_size=13,
        line_spacing=0,
    )
    t.set_fps(15)

    # -------------------------------------------------------------
    # 1. jb bios initialization phase
    # -------------------------------------------------------------
    t.toggle_show_cursor(False)
    time_now = datetime.now(ZoneInfo("Asia/Manila")).strftime("%Y")
    
    t.gen_text("JB BIOS v1.0.11 initializing", 1)
    t.gen_text(f"Copyright (C) {time_now}, \x1b[95m23arkve\x1b[0m", 2)
    t.gen_text("\x1b[94mJB OS ReadMe Terminal - Catppuccin Mocha Edition\x1b[0m", 4)
    t.gen_text("Krypton(tm) GIFCPU - 250Hz", 6)
    t.gen_text("Press \x1b[94mDEL\x1b[0m to enter SETUP, \x1b[94mESC\x1b[0m to skip Memory Test", 7)
    
    for i in range(0, 262144, 32768):
        t.delete_row(9)
        t.gen_text(f"Memory Test: {i}KB", 9, contin=True)
    t.delete_row(9)
    t.gen_text("Memory Test: \x1b[92m262144KB OK\x1b[0m", 9, count=5, contin=True)
    t.clone_frame(10)

    # -------------------------------------------------------------
    # 2. kernel boot sequence & vtks title logo
    # -------------------------------------------------------------
    t.clear_frame()
    t.gen_text("Initiating Boot Sequence ", 1, contin=True)
    t.gen_typing_text(".....", 1, contin=True, speed=1)
    
    # big centered "jb os" title effect in light blue (\x1b[96m) using vtks blocketo font
    t.gen_text("\x1b[96m", 1, count=0, contin=True)
    t.set_font(FONT_LOGO, 66)
    os_logo_text = "JB OS"
    mid_row = (t.num_rows + 1) // 2
    mid_col = (t.num_cols - len(os_logo_text) + 1) // 2
    effect_lines = gifos.effects.text_scramble_effect_lines(
        os_logo_text, 4, include_special=False
    )
    for i in range(len(effect_lines)):
        t.delete_row(mid_row + 1)
        t.gen_text(effect_lines[i], mid_row + 1, mid_col + 1)
    t.clone_frame(12)

    # -------------------------------------------------------------
    # 3. login phase
    # -------------------------------------------------------------
    t.set_font(FONT_MAIN, 13, line_spacing=0)
    t.clear_frame()
    t.gen_text("\x1b[93mJB OS v1.0.11 (tty1)\x1b[0m", 1, count=3)
    t.gen_text("login: ", 3, count=3)
    t.toggle_show_cursor(True)
    t.gen_typing_text("23arkve", 3, contin=True, speed=1)
    
    t.toggle_show_cursor(False)
    t.gen_text("password: ", 4, count=3)
    t.toggle_show_cursor(True)
    t.gen_typing_text("********", 4, contin=True, speed=1)
    
    t.toggle_show_cursor(False)
    login_time = datetime.now(ZoneInfo("Asia/Manila")).strftime("%a %b %d %H:%M:%S %Z %Y")
    t.gen_text(f"Last login: {login_time} on tty1", 6)
    t.clone_frame(8)

    # -------------------------------------------------------------
    # 4. profile fetch & details phase
    # -------------------------------------------------------------
    t.set_prompt("\x1b[95m23arkve\x1b[0m@\x1b[94mgithub\x1b[0m:~$ ")
    t.clear_frame()
    
    t.gen_prompt(1)
    prompt_col = t.curr_col
    t.toggle_show_cursor(True)
    
    # simulate syntax highlighted command input at top row
    t.gen_typing_text("\x1b[91mghfetc", 1, contin=True, speed=1)
    t.delete_row(1, prompt_col)
    t.gen_text("\x1b[92mghfetch\x1b[0m", 1, contin=True)
    t.gen_typing_text(" -u 23arkve", 1, contin=True, speed=1)
    t.clone_frame(5)
    t.toggle_show_cursor(False)

    # exact octocat mona lines
    mona_ascii = """
    \x1b[49m    \x1b[90;100m}}}}\x1b[49m   \x1b[90;100m}}}}\x1b[0m
    \x1b[49m    \x1b[90;100m}}}}}\x1b[49m \x1b[90;100m}}}}}\x1b[0m
    \x1b[49m   \x1b[90;100m}}}}}}}}}}}}}\x1b[0m
    \x1b[49m   \x1b[90;100m}}}}}}}}}}}}}}\x1b[0m
    \x1b[49m   \x1b[90;100m}}\x1b[37;47m}}}}}}}\x1b[90;100m}}}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}}\x1b[37;47m}}}}}}}}}}\x1b[90;100m}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}}\x1b[37;47m}\x1b[90;100m}\x1b[37;47m}}}}}\x1b[90;100m}\x1b[37;47m}}\x1b[90;100m}}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}\x1b[37;47m}}\x1b[90;100m}\x1b[37;47m}}}}}\x1b[90;100m}\x1b[37;47m}}}\x1b[90;100m}}}\x1b[0m
    \x1b[90;100m}}}\x1b[37;47m}}}}\x1b[90;100m}}}\x1b[37;47m}}}}}\x1b[90;100m}}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}\x1b[37;47m}}}}}\x1b[90;100m}}\x1b[37;47m}}}}}\x1b[90;100m}}}\x1b[0m
    \x1b[49m \x1b[90;100m}}\x1b[37;47m}}}}}}}}}}}}\x1b[90;100m}}}\x1b[0m
    \x1b[90;100m}\x1b[49m  \x1b[90;100m}}\x1b[37;47m}}}}}}}}\x1b[90;100m}}}\x1b[49m  \x1b[90;100m}\x1b[0m
    \x1b[49m        \x1b[90;100m}}}}}\x1b[0m
    \x1b[49m       \x1b[90;100m}}}}}}}\x1b[0m
    \x1b[49m       \x1b[90;100m}}}}}}}}\x1b[0m
    \x1b[49m      \x1b[90;100m}}}}}}}}}}\x1b[0m
    \x1b[49m     \x1b[90;100m}}}}}}}}}\x1b[0m
    \x1b[49m     \x1b[90;100m}}}}}}}}}}}}\x1b[0m
    \x1b[49m     \x1b[90;100m}}\x1b[49m \x1b[90;100m}}}}}}\x1b[49m \x1b[90;100m}}\x1b[0m
    \x1b[49m        \x1b[90;100m}}}}}}}\x1b[0m
    \x1b[49m         \x1b[90;100m}}}\x1b[49m \x1b[90;100m}}\x1b[0m"""
    
    # fetch live github stats if github_token environment variable is set
    gh_stats = None
    if os.getenv("GITHUB_TOKEN"):
        try:
            print("INFO: Fetching live GitHub stats for 23arkve...")
            gh_stats = gifos.utils.fetch_github_stats("23arkve")
        except Exception as e:
            print(f"Warning: Failed to fetch live GitHub stats: {e}")

    if gh_stats:
        top_langs = ", ".join([lang[0] for lang in gh_stats.languages_sorted[:4]])
        stats_block = f"""\x1b[96mUser Rating:  \x1b[93m{gh_stats.user_rank.level}\x1b[0m
    \x1b[96mTotal Stars:  \x1b[93m{gh_stats.total_stargazers}\x1b[0m
    \x1b[96mTotal Commits:\x1b[93m{gh_stats.total_commits_last_year}\x1b[0m
    \x1b[96mTotal PRs:    \x1b[93m{gh_stats.total_pull_requests_made}\x1b[0m
    \x1b[96mTop Languages:\x1b[93m{top_langs}\x1b[0m"""
    else:
        stats_block = """\x1b[96mUser Rating:  \x1b[93mA+\x1b[0m
    \x1b[96mTotal Stars:  \x1b[93m10\x1b[0m
    \x1b[96mTotal Commits:\x1b[93m100+\x1b[0m
    \x1b[96mTotal PRs:    \x1b[93m5\x1b[0m
    \x1b[96mTop Languages:\x1b[93mC, C++, JS/TS, Python\x1b[0m"""

    user_info_text = f"""
    \x1b[30;105m 23arkve@GitHub \x1b[0m
    -----------------------------------
    \x1b[96mName:      \x1b[93mBea\x1b[0m
    \x1b[96mRole:      \x1b[93mFrontend Dev\x1b[0m
    \x1b[96mEdu:       \x1b[93m4th Year CS @ UP Baguio\x1b[0m
    \x1b[96mFocus:     \x1b[93mReact, TailwindCSS, Figma, Next.js\x1b[0m
    \x1b[96mLanguages: \x1b[93mC, C++, JS/TS, Python, Java, PHP\x1b[0m
    \x1b[96mLearning:  \x1b[93mthree.js, p5.js, Spline\x1b[0m
    \x1b[96mDesign:    \x1b[93mFigma, Illustrator, Photoshop, Blender\x1b[0m
    \x1b[96mInterests: \x1b[93mphotography, side quests, walking\x1b[0m
    -----------------------------------
    \x1b[30;105m Contact \x1b[0m
    \x1b[96mLinkedIn:  \x1b[93mlinkedin.com/in/jbnovesteras\x1b[0m
    \x1b[96mEmail:     \x1b[93mjbnove@proton.me\x1b[0m
    -----------------------------------
    \x1b[30;105m GitHub Stats \x1b[0m
    {stats_block}
    """

    # generate octocat and user details starting at row 3 right below the command prompt
    t.gen_text(mona_ascii, 4)
    t.gen_text(user_info_text, 4, col_num=35, contin=True)
    
    # extended pause on stats screen (120 frames = ~8 seconds)
    t.clone_frame(120)

    # -------------------------------------------------------------
    # 5. closing comment
    # -------------------------------------------------------------
    t.gen_prompt(25)
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[92m# thank u for stopping by ! :D\x1b[0m", 25, contin=True, speed=1)
    
    # extended pause on closing comment (60 frames = ~4 seconds)
    t.clone_frame(60)

    # -------------------------------------------------------------
    # 6. reboot & output generation
    # -------------------------------------------------------------
    t.gen_prompt(25)
    t.toggle_show_cursor(True)
    t.gen_typing_text("reboot", 25, contin=True, speed=1)
    t.clone_frame(5)
    
    t.clear_frame()
    t.gen_text("\x1b[91mRestarting JB OS...\x1b[0m", 1)
    t.clone_frame(10)

    # save and output gif
    print("Generating terminal GIF...")
    t.gen_gif()

    readme_content = f"""<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./output.gif">
    <source media="(prefers-color-scheme: light)" srcset="./output.gif">
    <img alt="23arkve Terminal GIF" src="./output.gif" width="750">
  </picture>

  <p><sub><i>Generated automatically using <a href="https://github.com/x0rzavi/github-readme-terminal">x0rzavi/github-readme-terminal</a> (Catppuccin Mocha Theme)</i></sub></p>
</div>

---
"""
    with open("README.md", "w") as f:
        f.write(readme_content)
    print("SUCCESS: Updated README.md and generated output.gif!")

if __name__ == "__main__":
    main()