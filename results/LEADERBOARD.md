# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 2:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 314 windows, 8406 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 687 | 53.0 | 51.8 | $-130.28 | -1.9% | $869.72 | -0.5 | done | can't tell from luck |
| value_ev20 | 155 | 34.2 | 36.6 | $-180.14 | -11.6% | $819.86 | -1.1 | Sun 2:30 AM | too few trades (155/200) |
| reversal_15m_0.10pct | 833 | 52.9 | 51.9 | $-183.22 | -2.2% | $816.78 | -0.7 | done | can't tell from luck |
| value_ev10 | 401 | 38.2 | 40.5 | $-402.08 | -10.0% | $597.92 | -1.7 | done | can't tell from luck |
| value_ev5 | 600 | 39.8 | 42.2 | $-596.45 | -9.9% | $403.55 | -2.1 | done | losing for real |
| trend_filter | 466 | 45.1 | 50.3 | $-688.46 | -14.8% | $311.54 | -3.3 | done | losing for real |
| momentum_60m_0.30pct | 687 | 47.0 | 49.9 | $-714.76 | -10.4% | $285.24 | -2.8 | done | losing for real |
| coinflip | 1248 | 49.9 | 50.9 | $-767.96 | -6.2% | $232.04 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 833 | 47.1 | 49.9 | $-807.35 | -9.7% | $192.65 | -2.8 | done | losing for real |
| momentum_5m_0.00pct | 1248 | 48.5 | 51.3 | $-1200.16 | -9.6% | $-200.16 | -3.5 | done | losing for real |
| always_up | 1248 | 47.4 | 50.5 | $-1259.07 | -10.1% | $-259.07 | -3.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1888 | 46.5 | 49.3 | $-1870.34 |
| ETH | 2106 | 46.9 | 48.8 | $-2005.50 |
| SOL | 2187 | 47.9 | 49.4 | $-1807.40 |
| XRP | 2225 | 48.6 | 49.1 | $-1246.71 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
