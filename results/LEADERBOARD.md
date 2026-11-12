# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 7:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 150 windows, 3800 settled trades, 38 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 268 | 60.1 | 53.0 | $+285.86 | +10.7% | $1285.86 | +1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 366 | 56.8 | 52.3 | $+217.85 | +6.0% | $1217.85 | +1.2 | done | can't tell from luck |
| momentum_5m_0.00pct | 592 | 52.4 | 51.3 | $-135.44 | -2.3% | $864.56 | -0.6 | done | can't tell from luck |
| value_ev20 | 74 | 32.4 | 37.2 | $-143.54 | -19.4% | $856.46 | -1.4 | Sun 2:15 AM | too few trades (74/200) |
| coinflip | 592 | 51.0 | 50.9 | $-270.22 | -4.6% | $729.78 | -1.2 | done | can't tell from luck |
| value_ev10 | 199 | 36.7 | 40.7 | $-292.43 | -14.7% | $707.57 | -1.8 | Thu 7:00 AM | too few trades (199/200) |
| trend_filter | 193 | 41.5 | 49.2 | $-367.78 | -19.1% | $632.22 | -2.7 | Thu 8:15 AM | too few trades (193/200) |
| value_ev5 | 290 | 37.9 | 42.4 | $-429.73 | -14.8% | $570.27 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 268 | 39.9 | 49.3 | $-582.03 | -21.7% | $417.97 | -3.6 | done | losing for real |
| momentum_15m_0.10pct | 366 | 43.2 | 50.0 | $-610.91 | -16.7% | $389.09 | -3.3 | done | losing for real |
| always_up | 592 | 46.3 | 50.0 | $-708.02 | -12.0% | $291.98 | -3.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 815 | 45.8 | 49.6 | $-858.75 |
| ETH | 940 | 45.4 | 48.8 | $-1051.28 |
| SOL | 999 | 48.2 | 48.8 | $-755.28 |
| XRP | 1046 | 50.2 | 49.1 | $-371.10 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
