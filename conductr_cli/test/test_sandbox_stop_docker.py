from conductr_cli.test.cli_test_case import CliTestCase
from conductr_cli import sandbox_stop_docker, logging_setup
from conductr_cli.screen_utils import headline
from unittest.mock import patch, MagicMock


class TestSandboxStopCommand(CliTestCase):

    default_args = {
        'local_connection': True,
        'verbose': False,
        'quiet': False
    }

    def test_success(self):
        stdout = MagicMock()
        containers = ['cond-0', 'cond-1']

        with patch('conductr_cli.sandbox_common.resolve_running_docker_containers', return_value=containers), \
                patch('conductr_cli.terminal.docker_rm') as mock_docker_rm:
            logging_setup.configure_logging(MagicMock(**self.default_args), stdout)
            sandbox_stop_docker.stop(MagicMock(**self.default_args))

        self.assertEqual(headline('Stopping ConductR') + '\n', self.output(stdout))
        mock_docker_rm.assert_called_once_with(containers)
