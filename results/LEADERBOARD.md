# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 8:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 68 windows, 1680 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 118 | 60.2 | 52.3 | $+150.12 | +12.7% | $1150.12 | +1.4 | Wed 7:15 PM | too few trades (118/200) |
| momentum_5m_0.00pct | 264 | 54.5 | 51.0 | $+95.59 | +3.6% | $1095.59 | +0.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 154 | 55.2 | 51.6 | $+72.50 | +4.7% | $1072.50 | +0.6 | Wed 12:45 PM | too few trades (154/200) |
| value_ev10 | 89 | 42.7 | 39.1 | $+25.25 | +2.8% | $1025.25 | +0.2 | Thu 4:30 AM | too few trades (89/200) |
| value_ev20 | 40 | 35.0 | 35.6 | $-23.85 | -6.0% | $976.15 | -0.3 | Sat 1:45 AM | too few trades (40/200) |
| value_ev5 | 125 | 40.0 | 40.9 | $-81.98 | -6.6% | $918.02 | -0.6 | Wed 5:45 PM | too few trades (125/200) |
| trend_filter | 90 | 44.4 | 49.1 | $-112.79 | -12.5% | $887.21 | -1.2 | Thu 4:00 AM | too few trades (90/200) |
| coinflip | 264 | 50.0 | 51.5 | $-163.61 | -6.2% | $836.39 | -1.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 154 | 44.8 | 49.8 | $-188.70 | -12.3% | $811.30 | -1.5 | Wed 12:45 PM | too few trades (154/200) |
| momentum_60m_0.30pct | 118 | 39.8 | 49.1 | $-238.98 | -20.3% | $761.02 | -2.2 | Wed 7:15 PM | too few trades (118/200) |
| always_up | 264 | 43.2 | 49.9 | $-437.53 | -16.6% | $562.47 | -2.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 347 | 47.0 | 49.6 | $-118.02 |
| ETH | 400 | 45.8 | 48.4 | $-274.79 |
| SOL | 459 | 48.1 | 48.1 | $-302.59 |
| XRP | 474 | 50.0 | 48.3 | $-208.58 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
