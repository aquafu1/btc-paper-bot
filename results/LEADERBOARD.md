# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 1:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 213 windows, 5547 settled trades, 72 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 547 | 56.7 | 52.6 | $+245.14 | +4.5% | $1245.14 | +1.1 | done | can't tell from luck |
| reversal_60m_0.30pct | 428 | 55.1 | 52.6 | $+71.71 | +1.7% | $1071.71 | +0.4 | done | can't tell from luck |
| value_ev20 | 104 | 33.7 | 36.9 | $-137.53 | -13.2% | $862.47 | -1.1 | Sun 6:30 AM | too few trades (104/200) |
| value_ev10 | 274 | 36.5 | 40.8 | $-390.93 | -14.3% | $609.07 | -2.0 | done | losing for real |
| trend_filter | 287 | 44.3 | 50.0 | $-431.73 | -15.0% | $568.27 | -2.6 | done | losing for real |
| coinflip | 844 | 50.1 | 51.0 | $-500.77 | -5.9% | $499.23 | -1.8 | done | can't tell from luck |
| value_ev5 | 400 | 38.8 | 42.6 | $-514.10 | -12.9% | $485.90 | -2.3 | done | losing for real |
| momentum_5m_0.00pct | 844 | 50.4 | 51.5 | $-525.26 | -6.2% | $474.74 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 428 | 44.9 | 49.6 | $-574.92 | -13.4% | $425.08 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 547 | 43.3 | 49.7 | $-892.45 | -16.3% | $107.55 | -3.9 | done | losing for real |
| always_up | 844 | 46.4 | 50.2 | $-989.42 | -11.7% | $10.58 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1234 | 45.9 | 49.7 | $-1340.25 |
| ETH | 1382 | 46.5 | 48.9 | $-1325.46 |
| SOL | 1430 | 47.7 | 49.3 | $-1272.85 |
| XRP | 1501 | 49.4 | 49.3 | $-701.71 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
