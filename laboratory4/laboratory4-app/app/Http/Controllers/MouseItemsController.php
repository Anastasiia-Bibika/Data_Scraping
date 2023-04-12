<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\MouseItem;

class MouseItemsController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        $items = MouseItem::all();
        return view('mouse.index', ['items' => $items]);
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        return view('mouse.create');
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        $mouse = MouseItem::create([
            'name' => $request->input('name'),
            'price' => $request->input('price'),
            'url' => $request->input('url'),
            'image_urls' => $request->input('image_urls'),
            'img' => $request->input('img'),
        ]);
        return redirect(route('mouse.index'));
    }

    /**
     * Display the specified resource.
     */
    public function show(string $id)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(string $id)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, string $id)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(string $id)
    {
        //
    }
}
