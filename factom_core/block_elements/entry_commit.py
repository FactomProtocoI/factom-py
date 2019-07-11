class EntryCommit:

    ECID = 0x03
    BITLENGTH = 136

    def __init__(self,timestamp: bytes, entry_hash: bytes, ec_spent: int, ec_public_key: bytes, signature: bytes,
                 **kwargs):
        # Required fields. Must be in every EntryCommit
        self.timestamp = timestamp
        self.entry_hash = entry_hash
        self.ec_spent = ec_spent
        self.ec_public_key = ec_public_key
        self.signature = signature
        # TODO: assert they're all here
        # TODO: use kwargs for some optional metadata

    def marshal(self):
        """Marshals the EntryCommit according to the byte-level representation shown at
        https://github.com/FactomProject/FactomDocs/blob/master/factomDataStructureDetails.md#entry-commit
        """
        buf = bytearray()
        buf.append(0x00)
        buf.extend(self.timestamp)
        buf.extend(self.entry_hash)
        buf.append(self.ec_spent)
        buf.extend(self.ec_public_key)
        buf.extend(self.signature)
        return bytes(buf)

    @classmethod
    def unmarshal(cls, raw: bytes):
        """Returns a new EntryCommit object, unmarshalling given bytes according to:
        https://github.com/FactomProject/FactomDocs/blob/master/factomDataStructureDetails.md#entry-commit
        """
        data = raw[1:]  # skip single byte version, probably just 0x00 anyways
        timestamp, data = data[:6], data[6:]
        entry_hash, data = data[:32], data[32:]
        ec_spent, data = data[:1], data[1:]
        ec_spent = int.from_bytes(ec_spent, byteorder='big')
        assert ec_spent < 11, 'Invalid EC spent ({}) for entry: {}'.format(ec_spent, entry_hash.hex())
        ec_public_key, data = data[:32], data[32:]
        signature, data = data[:64], data[64:]  # covers version through ec spent
        assert len(data) == 0, 'Extra bytes remaining!'

        return EntryCommit(
            timestamp=timestamp,
            entry_hash=entry_hash,
            ec_spent=ec_spent,
            ec_public_key=ec_public_key,
            signature=signature
        )

    def to_dict(self):
        pass  # TODO: Implement EntryCommit.to_dict()

    def __str__(self):
        # TODO: convert timestamp to readable and EC Public Key to its base58 address
        return '{}(timestamp={}, entry_hash={}, ec_public_key={})'.format(
            self.__class__.__name__, self.timestamp, self.entry_hash.hex(), self.ec_public_key.hex())

