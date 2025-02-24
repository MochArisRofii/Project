# Generated by Django 5.0.6 on 2024-05-17 03:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sekolah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=99)),
                ('alamat', models.CharField(blank=True, max_length=199, null=True)),
                ('kota', models.CharField(blank=True, max_length=99, null=True)),
                ('provinsi', models.CharField(blank=True, max_length=99, null=True)),
                ('no_telp', models.CharField(blank=True, max_length=19, null=True)),
                ('email', models.EmailField(blank=True, max_length=99, null=True)),
                ('website', models.URLField(blank=True, max_length=99, null=True)),
                ('catatan', models.CharField(blank=True, max_length=199, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PelanggaranKategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=99)),
                ('poin', models.PositiveIntegerField()),
                ('pesan', models.CharField(blank=True, max_length=199, null=True)),
                ('catatan', models.CharField(blank=True, max_length=199, null=True)),
                ('sekolah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pelanggaran_Siswa.sekolah')),
            ],
        ),
        migrations.CreateModel(
            name='Kelas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=99)),
                ('tingkat', models.PositiveSmallIntegerField()),
                ('catatan', models.CharField(blank=True, max_length=199, null=True)),
                ('sekolah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pelanggaran_Siswa.sekolah')),
            ],
        ),
        migrations.CreateModel(
            name='Siswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nis', models.CharField(max_length=19)),
                ('nama', models.CharField(max_length=99)),
                ('nama_ortu', models.CharField(blank=True, max_length=99, null=True)),
                ('hp_ortu', models.CharField(blank=True, max_length=19, null=True)),
                ('email_ortu', models.EmailField(blank=True, max_length=99, null=True)),
                ('catatan', models.CharField(blank=True, max_length=199, null=True)),
                ('kelas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Pelanggaran_Siswa.kelas')),
                ('sekolah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pelanggaran_Siswa.sekolah')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=49, unique=True)),
                ('nama', models.CharField(blank=True, max_length=99, null=True)),
                ('email', models.EmailField(blank=True, max_length=99, null=True)),
                ('no_hp', models.CharField(blank=True, max_length=19, null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('jabatan', models.CharField(blank=True, max_length=99, null=True)),
                ('catatan', models.CharField(blank=True, max_length=199, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('sekolah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pelanggaran_Siswa.sekolah')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pelanggaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tgl_jam', models.DateTimeField()),
                ('poin', models.PositiveIntegerField()),
                ('catatan', models.CharField(blank=True, max_length=199, null=True)),
                ('kelas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pelanggaran_Siswa.kelas')),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pelanggaran_Siswa.pelanggarankategori')),
                ('sekolah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pelanggaran_Siswa.sekolah')),
                ('siswa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pelanggaran_Siswa.siswa')),
                ('petugas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
