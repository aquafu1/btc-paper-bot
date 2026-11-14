# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 1:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 309 windows, 8251 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 817 | 53.2 | 51.7 | $-116.50 | -1.4% | $883.50 | -0.4 | done | can't tell from luck |
| reversal_60m_0.30pct | 672 | 53.0 | 51.7 | $-121.55 | -1.8% | $878.45 | -0.5 | done | can't tell from luck |
| value_ev20 | 152 | 34.9 | 36.5 | $-150.14 | -9.9% | $849.86 | -1.0 | Sun 3:00 AM | too few trades (152/200) |
| value_ev10 | 395 | 38.2 | 40.5 | $-386.52 | -9.8% | $613.48 | -1.7 | done | can't tell from luck |
| value_ev5 | 588 | 39.5 | 42.2 | $-632.64 | -10.8% | $367.36 | -2.3 | done | losing for real |
| trend_filter | 454 | 45.4 | 50.4 | $-652.16 | -14.4% | $347.84 | -3.1 | done | losing for real |
| momentum_60m_0.30pct | 672 | 47.0 | 50.0 | $-712.10 | -10.6% | $287.90 | -2.8 | done | losing for real |
| coinflip | 1228 | 50.0 | 50.9 | $-737.23 | -6.0% | $262.77 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 817 | 46.8 | 50.0 | $-862.60 | -10.6% | $137.40 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 1228 | 48.7 | 51.4 | $-1139.90 | -9.3% | $-139.90 | -3.4 | done | losing for real |
| always_up | 1228 | 47.6 | 50.4 | $-1200.35 | -9.8% | $-200.35 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1855 | 46.5 | 49.3 | $-1825.09 |
| ETH | 2065 | 47.1 | 48.8 | $-1918.93 |
| SOL | 2145 | 48.0 | 49.4 | $-1712.86 |
| XRP | 2186 | 48.6 | 49.1 | $-1254.81 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
