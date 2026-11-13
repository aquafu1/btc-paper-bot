# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 10:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 248 windows, 6496 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 642 | 55.5 | 52.2 | $+141.87 | +2.2% | $1141.87 | +0.6 | done | can't tell from luck |
| reversal_60m_0.30pct | 516 | 53.5 | 52.1 | $-71.41 | -1.4% | $928.59 | -0.3 | done | can't tell from luck |
| value_ev20 | 114 | 34.2 | 36.7 | $-120.27 | -10.6% | $879.73 | -0.9 | Sun 12:30 PM | too few trades (114/200) |
| value_ev10 | 310 | 37.1 | 40.9 | $-393.26 | -12.7% | $606.74 | -1.9 | done | can't tell from luck |
| trend_filter | 343 | 46.1 | 50.5 | $-439.72 | -12.8% | $560.28 | -2.4 | done | losing for real |
| value_ev5 | 458 | 39.3 | 42.6 | $-535.11 | -11.7% | $464.89 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 516 | 46.5 | 50.0 | $-589.15 | -11.4% | $410.85 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 985 | 50.2 | 51.6 | $-684.59 | -7.0% | $315.41 | -2.3 | done | losing for real |
| coinflip | 985 | 49.3 | 50.9 | $-742.71 | -7.5% | $257.29 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 642 | 44.5 | 50.0 | $-943.26 | -14.7% | $56.74 | -3.8 | done | losing for real |
| always_up | 985 | 46.8 | 50.5 | $-1149.11 | -11.7% | $-149.11 | -3.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1454 | 46.6 | 49.8 | $-1510.42 |
| ETH | 1627 | 46.8 | 49.1 | $-1676.94 |
| SOL | 1679 | 48.1 | 49.4 | $-1374.05 |
| XRP | 1736 | 48.7 | 49.2 | $-965.29 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
