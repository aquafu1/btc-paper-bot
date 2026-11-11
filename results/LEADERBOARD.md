# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 5:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 97 windows, 2457 settled trades, 68 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 181 | 59.1 | 52.7 | $+172.93 | +9.6% | $1172.93 | +1.4 | Wed 5:30 PM | too few trades (181/200) |
| momentum_5m_0.00pct | 380 | 54.7 | 50.8 | $+152.60 | +4.0% | $1152.60 | +0.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 234 | 56.8 | 52.3 | $+152.20 | +6.5% | $1152.20 | +1.0 | done | can't tell from luck |
| value_ev10 | 130 | 39.2 | 40.3 | $-95.89 | -7.4% | $904.11 | -0.7 | Thu 4:00 AM | too few trades (130/200) |
| value_ev20 | 48 | 29.2 | 36.2 | $-103.85 | -21.6% | $896.15 | -1.2 | Sat 6:15 PM | too few trades (48/200) |
| trend_filter | 132 | 46.2 | 49.1 | $-118.60 | -9.0% | $881.40 | -1.0 | Thu 3:15 AM | too few trades (132/200) |
| coinflip | 380 | 50.3 | 51.4 | $-228.19 | -6.0% | $771.81 | -1.2 | done | can't tell from luck |
| value_ev5 | 177 | 37.3 | 41.7 | $-251.33 | -14.2% | $748.67 | -1.7 | Wed 6:15 PM | too few trades (177/200) |
| momentum_60m_0.30pct | 181 | 40.9 | 49.2 | $-352.13 | -19.5% | $647.87 | -2.6 | Wed 5:30 PM | too few trades (181/200) |
| momentum_15m_0.10pct | 234 | 43.2 | 49.6 | $-368.50 | -15.7% | $631.50 | -2.4 | done | losing for real |
| always_up | 380 | 46.3 | 50.2 | $-426.83 | -11.2% | $573.17 | -2.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 525 | 47.0 | 49.7 | $-297.93 |
| ETH | 599 | 46.2 | 48.8 | $-448.85 |
| SOL | 659 | 48.9 | 48.4 | $-380.46 |
| XRP | 674 | 49.9 | 48.9 | $-340.34 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
