fn input_path() -> String {
    std::env::args().nth(1).unwrap()
}

fn read_text() -> String {
    std::fs::read_to_string(input_path()).unwrap().trim_end().to_string()
}

// Rust has no MD5 in its standard library, so here is a small one
fn md5(message: &[u8], k: &[u32; 64]) -> [u8; 16] {
    const S: [u32; 64] = [
        7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
        5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
        4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
        6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21,
    ];

    let mut data = message.to_vec();
    let bit_length = (message.len() as u64) * 8;
    data.push(0x80);
    while data.len() % 64 != 56 {
        data.push(0);
    }
    data.extend_from_slice(&bit_length.to_le_bytes());

    let (mut a0, mut b0, mut c0, mut d0) = (0x67452301u32, 0xefcdab89u32, 0x98badcfeu32, 0x10325476u32);
    for chunk in data.chunks(64) {
        let m: Vec<u32> = chunk.chunks(4).map(|word| u32::from_le_bytes(word.try_into().unwrap())).collect();
        let (mut a, mut b, mut c, mut d) = (a0, b0, c0, d0);
        for i in 0..64 {
            let (f, g) = if i < 16 {
                ((b & c) | (!b & d), i)
            } else if i < 32 {
                ((d & b) | (!d & c), (5 * i + 1) % 16)
            } else if i < 48 {
                (b ^ c ^ d, (3 * i + 5) % 16)
            } else {
                (c ^ (b | !d), (7 * i) % 16)
            };
            let f = f.wrapping_add(a).wrapping_add(k[i]).wrapping_add(m[g]);
            a = d;
            d = c;
            c = b;
            b = b.wrapping_add(f.rotate_left(S[i]));
        }
        a0 = a0.wrapping_add(a);
        b0 = b0.wrapping_add(b);
        c0 = c0.wrapping_add(c);
        d0 = d0.wrapping_add(d);
    }

    let mut digest = [0u8; 16];
    digest[0..4].copy_from_slice(&a0.to_le_bytes());
    digest[4..8].copy_from_slice(&b0.to_le_bytes());
    digest[8..12].copy_from_slice(&c0.to_le_bytes());
    digest[12..16].copy_from_slice(&d0.to_le_bytes());
    digest
}

fn main() {
    let file_content = read_text();

    let mut k = [0u32; 64];
    for i in 0..64 {
        k[i] = (((i + 1) as f64).sin().abs() * 4294967296.0) as u32;
    }

    let mut part_1_res = 0;
    let part_2_res;
    let mut part_1_done = false;

    let mut count = 1;
    loop {
        let res = md5(format!("{}{}", file_content, count).as_bytes(), &k);
        // Each byte is two hex digits
        let five_zeros = res[0] == 0 && res[1] == 0 && res[2] < 16;
        let six_zeros = res[0] == 0 && res[1] == 0 && res[2] == 0;
        if five_zeros && !part_1_done {
            part_1_res = count;
            part_1_done = true;
        }
        if six_zeros {
            part_2_res = count;
            break;
        }
        count += 1;
    }

    println!("Part 1 res: {}", part_1_res);
    println!("Part 2 res: {}", part_2_res);
}
