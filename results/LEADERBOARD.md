# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 4:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 272 windows, 7125 settled trades, 71 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 700 | 54.4 | 52.3 | $+11.64 | +0.2% | $1011.64 | +0.0 | done | can't tell from luck |
| value_ev20 | 128 | 35.9 | 37.0 | $-98.42 | -7.7% | $901.58 | -0.7 | Sun 8:45 AM | too few trades (128/200) |
| reversal_60m_0.30pct | 569 | 52.2 | 52.2 | $-236.75 | -4.2% | $763.25 | -1.0 | done | can't tell from luck |
| value_ev10 | 343 | 38.5 | 40.9 | $-327.16 | -9.5% | $672.84 | -1.5 | done | can't tell from luck |
| trend_filter | 371 | 46.9 | 50.2 | $-409.54 | -11.0% | $590.46 | -2.2 | done | losing for real |
| value_ev5 | 505 | 40.4 | 42.5 | $-451.20 | -8.9% | $548.80 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 569 | 47.8 | 49.7 | $-489.94 | -8.6% | $510.06 | -2.1 | done | losing for real |
| coinflip | 1080 | 49.5 | 50.9 | $-743.05 | -6.9% | $256.95 | -2.3 | done | losing for real |
| momentum_5m_0.00pct | 1080 | 49.9 | 51.5 | $-762.44 | -7.1% | $237.56 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 700 | 45.6 | 49.7 | $-852.84 | -12.2% | $147.16 | -3.3 | done | losing for real |
| always_up | 1080 | 47.0 | 50.2 | $-1132.65 | -10.5% | $-132.65 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1588 | 46.7 | 49.6 | $-1608.61 |
| ETH | 1778 | 46.9 | 49.0 | $-1719.19 |
| SOL | 1847 | 48.4 | 49.3 | $-1334.70 |
| XRP | 1912 | 49.1 | 49.1 | $-829.85 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
