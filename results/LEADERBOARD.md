# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 12:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 403 windows, 11034 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 199 | 36.7 | 36.5 | $-56.95 | -2.9% | $943.05 | -0.3 | Sun 1:15 AM | too few trades (199/200) |
| value_ev10 | 519 | 40.5 | 40.5 | $-174.41 | -3.4% | $825.59 | -0.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 939 | 50.7 | 49.8 | $-220.92 | -2.4% | $779.08 | -0.7 | done | can't tell from luck |
| value_ev5 | 780 | 42.1 | 42.2 | $-293.06 | -3.8% | $706.94 | -0.9 | done | can't tell from luck |
| trend_filter | 626 | 50.2 | 50.6 | $-305.23 | -4.9% | $694.77 | -1.2 | done | can't tell from luck |
| momentum_15m_0.10pct | 1110 | 49.5 | 49.8 | $-465.80 | -4.2% | $534.20 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1110 | 50.5 | 52.0 | $-726.74 | -6.5% | $273.26 | -2.3 | done | losing for real |
| coinflip | 1604 | 50.1 | 50.9 | $-791.97 | -4.9% | $208.03 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 939 | 49.3 | 52.1 | $-837.36 | -8.9% | $162.64 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 1604 | 50.1 | 51.6 | $-1012.85 | -6.3% | $-12.85 | -2.6 | done | losing for real |
| always_up | 1604 | 46.0 | 50.8 | $-2030.01 | -12.7% | $-1030.01 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2491 | 47.9 | 49.5 | $-1672.50 |
| ETH | 2773 | 48.0 | 49.0 | $-1658.95 |
| SOL | 2852 | 48.0 | 49.5 | $-2087.91 |
| XRP | 2918 | 48.9 | 49.3 | $-1495.95 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
