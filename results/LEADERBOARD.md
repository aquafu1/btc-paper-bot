# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 12:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 304 windows, 8124 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 151 | 35.1 | 36.5 | $-140.14 | -9.3% | $859.86 | -0.9 | Sun 2:00 AM | too few trades (151/200) |
| reversal_60m_0.30pct | 664 | 52.7 | 51.7 | $-173.75 | -2.6% | $826.25 | -0.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 803 | 53.1 | 51.9 | $-173.81 | -2.2% | $826.19 | -0.6 | done | can't tell from luck |
| value_ev10 | 390 | 38.7 | 40.5 | $-336.52 | -8.6% | $663.48 | -1.4 | done | can't tell from luck |
| value_ev5 | 577 | 40.0 | 42.2 | $-547.82 | -9.5% | $452.18 | -2.0 | done | losing for real |
| trend_filter | 448 | 45.8 | 50.3 | $-606.14 | -13.5% | $393.86 | -2.9 | done | losing for real |
| momentum_60m_0.30pct | 664 | 47.3 | 49.9 | $-675.35 | -10.2% | $324.65 | -2.7 | done | losing for real |
| coinflip | 1208 | 50.1 | 50.9 | $-710.72 | -5.9% | $289.28 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 803 | 46.9 | 49.9 | $-804.23 | -10.0% | $195.77 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 1208 | 48.8 | 51.3 | $-1074.75 | -8.9% | $-74.75 | -3.2 | done | losing for real |
| always_up | 1208 | 47.3 | 50.4 | $-1253.81 | -10.4% | $-253.81 | -3.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1826 | 46.5 | 49.3 | $-1783.98 |
| ETH | 2032 | 47.2 | 48.8 | $-1829.09 |
| SOL | 2107 | 48.1 | 49.4 | $-1683.30 |
| XRP | 2159 | 48.6 | 49.1 | $-1200.65 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
