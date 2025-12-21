from .utils import check_output, PrettyCount, SUFFIX
from argparse import ArgumentParser, Namespace
from loguru import logger
from subprocess import run, PIPE
from pathlib3x import Path


def get_subrem_args(input_file: Path, output_file: Path):
    return [
        'mkvmerge',
        '-o',
       f'{output_file}',
        '--no-subtitles',
        f'{input_file}'
    ]


def subtitle_remove_task(output_dir: Path, file_name: str|Path):
    input_file = Path(file_name)
    output_file = output_dir / input_file.name
    if input_file.exists():
        args = get_subrem_args(input_file, output_file)
        logger.info(f'command: {' '.join(args)}')
        res = run(args, stdout=PIPE)
        logger.info(f"{res.stdout.decode("utf-8")}")
    else:
        raise FileNotFoundError(f"file {input_file} not found!")

def subtitle_remove_file(output_dir, file, msg):
    try:
        logger.info(msg)
        subtitle_remove_task(output_dir, file)
    except FileNotFoundError as err:
        logger.error(err)

def subtitle_remove_files(current_dir, files):
    output_dir = check_output(current_dir)
    pretty_count = PrettyCount(files)
    for count, file in pretty_count:
        msg = f'{count} removing subtitle from file "{file}"'
        subtitle_remove_file(output_dir, file, msg)

def subtitle_remove(argv: Namespace):
    current_dir = '.'
    if argv.files:
        files = [Path(file) for file in argv.files]
        files = [file for file in files if file.suffix.lower() in SUFFIX]
        subtitle_remove_files(current_dir, files)
    elif argv.file:
        subtitle_remove_files(current_dir, [argv.file])
    elif argv.directory:
        input_dir = Path(argv.directory)
        files = [file for file in input_dir.iterdir() if file.suffix.lower() in SUFFIX]
        subtitle_remove_files(input_dir, files)
    else:
        output_dir = Path('.')
        [subtitle_remove_task(output_dir, file)
         for file in output_dir.glob(r"*.mkv")]


def main(argv: Namespace):
    if argv.subtitle_remove:
        subtitle_remove(argv)

def app():

    NAME_PROG='subedit'
    parser = ArgumentParser(
            prog=f'{NAME_PROG}',
            usage=f'{NAME_PROG} [FLAG] [ARGS]',
            description='Programa usado para remover as legendas de vídeos',
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--subtitle-remove', '-r',
                        action='store_true',
                        help='Flag para remover todas as legendas de um arquivo `mkv`.')
    parser.add_argument('-d', '--directory',
                        help='Indica o diretorio que deve ser trabalhado')
    parser.add_argument('-f', '--file',
                        help='Indica o arquivo de entrada')
    parser.add_argument('-F', '--files',
                        nargs='*',
                        help='Para passar mais de um arquivo')
    args = parser.parse_args()

    main(args)

if __name__ == '__main__':
    app()
