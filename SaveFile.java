    public boolean data2File(int[] rgbaData) {
        String addr = "/mnt/sdcard/" + "edited_picture.txt";
        mMediaFileUri = Uri.parse("file://" + addr);
        File f = new File(addr);
        if (f.exists()) {
            f.delete();
        }

        try {
            f.createNewFile();
            ByteArrayOutputStream bos = new ByteArrayOutputStream();
            byte[] bitmapdata = new byte[4 * rgbaData.length];
            for (int i = 0; i < rgbaData.length; i++) {
                for (int j = 0; j < 4; j++) {
                    bitmapdata[i * 4 + j] = (byte) (rgbaData[i] >> 8 * (3 - j) & 0xFF);
                }
            }

            FileOutputStream fos = new FileOutputStream(f);
            fos.write(bitmapdata);
            fos.flush();
            fos.close();
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
        return true;
    }



    public boolean bitmap2File(Bitmap bitmap) {
        String addr = "/mnt/sdcard/" + "edited_picture.png";
        mMediaFileUri = Uri.parse("file://" + addr);
        File f = new File(addr);
        if (f.exists()) {
            f.delete();
        }

        try {
            f.createNewFile();
            ByteArrayOutputStream bos = new ByteArrayOutputStream();
            bitmap.compress(Bitmap.CompressFormat.PNG, 100, bos);
            byte[] bitmapdata = bos.toByteArray();
            FileOutputStream fos = new FileOutputStream(f);
            fos.write(bitmapdata);
            fos.flush();
            fos.close();
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
//        if (bitmap != null && !bitmap.isRecycled()) {
//            bitmap.recycle();
//        }
        return true;
    }
