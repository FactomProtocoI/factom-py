import unittest

from factom_core.messages.block_syncing import DirectoryBlockState, DirectoryBlockStateRequest


class TestDirectoryBlockState(unittest.TestCase):

    test_data = "14016bc45d142f00fa92e5a2fdc025295a9a1705a288dc1043a1a3506a6526c3ae4ad1f181643db8190ecb5726d84fa9d63a" \
                "52a2022c3d1d90d750fe1ef77c5b7aaf0963838de84b6e9f073303e1d9c915b67a9be2bc69cd032cafafb5c5574420fdbd3f" \
                "63a8ca19b35edeea016e806a0000000a00000004000000000000000000000000000000000000000000000000000000000000" \
                "000a60d6c075925bbd2ddaf3b8c6737225d9df1963d0d098e10b67605d557857fc5200000000000000000000000000000000" \
                "0000000000000000000000000000000c96131286eb49d4eb587a7dbce7a6af968b52fa0b0a9f31be9c4ff6ce5096ce680000" \
                "00000000000000000000000000000000000000000000000000000000000f05c7a500db98dfe393b296998b7d9b74e8f2d2cf" \
                "eacd1d44c05cfb50bd2cbaf3df3ade9eec4b08d5379cc64270c30ea7315d8a8a1a69efe2b98a60ecdd69e604027a0aa245d4" \
                "bd893e3b50bc642827524f867819ffd66e3bf57d62d251f98a29000000000000000000000000000000000000000000000000" \
                "000000000000000a3975db81e58939290e9399d319d8e946b8bf6d26ab9e7506a176035dc8dd02ff0000000a000000000200" \
                "0000830100000000000000000000000000000000000000000000000000000000000000000426a802617848d4d16d87830fc5" \
                "21f4d136bb2d0c352850919c2679f189613a3dea02b1f44ee668e165e2005ba8fa3473a814db4c6b40d9631a5917d44f59cf" \
                "0f65411dbbec312a110b5a43afff9d48ae967f0662a1797beee140d921b75702000100000000000000000000000000000000" \
                "0000000000000000000000000000000fbd99abfabe12023b57c933bbb8a54dce5e3fe03ec048c9d47279615dc6ab785312bf" \
                "ddc1e888a144352db3e50366ae3f022e5a7abe9d3ad911d66fddbbdfd2417cdf1f82f8446985333d6ee6141cba7907c8065d" \
                "34cc45bc14b39749038d791800000000000a2be80000000a00000000010000001402014f8ad10e2000000000000000000000" \
                "000000000000000000000000000000000000000000000000000000000000000000000c898b0672bb93057a2dec036ee99ef1" \
                "a2cae3fcea76733b0f3272e2f5c69bd0e8b88eb7b3fc0c1899e1e4603b04ce0820f2a14b754df75587164d6dfb577b0d19ec" \
                "d06bcf6041c4206d59e249b7442f46254063b9e68d6fef4b7d233ab8f6c8c00000000a00000000000000000e000000000000" \
                "01b10000010101020300014f8ad36d8d0503fe82359416fc8caecc4a33fbbe94b78f02929e91cbbd022a3c5cab685f6b0117" \
                "ef7a21d1a616d65e6b73f3c6a7ad5c49340a6c2592872020ec60767ff00d7d0bb90cd75fa38d6669deb8a23c31ed04524cde" \
                "e8574b4bb2576e5a1b7768855e1a07e89c62ebfb6abee3bf4d9e5cdee3b91c2390ab400c37f0f5f40201509d0d0300014f8a" \
                "d36d8fa479f8d5d76be64f1a82d0a1f9bdcc2d29ab9507811660e095a8423a515d877a0117ef7a21d1a616d65e6b73f3c6a7" \
                "ad5c49340a6c2592872020ec60767ff00d7dcac9dc9364259903c19f99f4f65c407e3345e9f4a45336c366947ca7dbc6ff5a" \
                "c474a061030922d625f2af03bedf8f812032e2647fa9c7a4d7de34481eef4a000300014f8ad36d90a952983ddf6331a705b7" \
                "62f30cd01265b23ec5ce98b5398326bf4b14f3a708f60117ef7a21d1a616d65e6b73f3c6a7ad5c49340a6c2592872020ec60" \
                "767ff00d7d8d4d4ce70cc7e699d1a49269228d5c058002337962d0440d0cd2b9d4b8f196a750b703928a61160f4507275730" \
                "5fec2db9a5f670a44f0509b69d6ad2fc0fdd000103010401050106010701080109010a00000001df3ade9eec4b08d5379cc6" \
                "4270c30ea7315d8a8a1a69efe2b98a60ecdd69e6042f2425b5ee042bbb6493907377d551ad238b8def9fdfcfbbb30fcba7e5" \
                "a0448eef7646f2f9251c9e50e19ab9343c25eb88c241aa49b7ca779c2318b8ccce1f8abbd9f1adf24beb48367df16b9556ad" \
                "6e177f5b356aee4f37982b49c56973b767000000030000000a000000040503fe82359416fc8caecc4a33fbbe94b78f02929e" \
                "91cbbd022a3c5cab685f6ba479f8d5d76be64f1a82d0a1f9bdcc2d29ab9507811660e095a8423a515d877aa952983ddf6331" \
                "a705b762f30cd01265b23ec5ce98b5398326bf4b14f3a708f600000000000000000000000000000000000000000000000000" \
                "0000000000000300000000000000010426a802617848d4d16d87830fc521f4d136bb2d0c352850919c2679f189613a5d5d9d" \
                "d7628be37d604436bb4754e49c29ad14acf2d04f12df88d46fcc39ea53a22b4f2b7bf0687a7ca0f3dbcafdec7d6b295ea2b0" \
                "ba8519c03321f10ad08f06"

    def test_unmarshal(self):
        expected_height = 10
        msg = DirectoryBlockState.unmarshal(bytes.fromhex(self.test_data))
        assert msg.timestamp.hex() == "016bc45d142f"
        assert msg.directory_block.header.height == expected_height
        assert msg.admin_block.header.height == expected_height
        assert msg.factoid_block.header.height == expected_height
        assert msg.entry_credit_block.header.height == expected_height
        for entry_block in msg.entry_blocks:
            assert entry_block.header.height == expected_height

    def test_marshal(self):
        msg = DirectoryBlockState.unmarshal(bytes.fromhex(self.test_data))
        assert msg.marshal() == bytes.fromhex(self.test_data)


class TestDirectoryBlockStateRequest(unittest.TestCase):

    test_data = "15016bc45d142f0123456789012345"

    def test_unmarshal(self):
        msg = DirectoryBlockStateRequest.unmarshal(bytes.fromhex(self.test_data))
        assert msg.timestamp.hex() == "016bc45d142f"
        assert msg.block_height_start == 19088743
        assert msg.block_height_end == 2298553157

    def test_marshal(self):
        msg = DirectoryBlockStateRequest.unmarshal(bytes.fromhex(self.test_data))
        assert msg.marshal() == bytes.fromhex(self.test_data)
