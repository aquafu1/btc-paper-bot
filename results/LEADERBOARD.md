# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 7:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 67 windows, 1663 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 116 | 59.5 | 52.1 | $+139.73 | +12.0% | $1139.73 | +1.3 | Wed 7:45 PM | too few trades (116/200) |
| momentum_5m_0.00pct | 261 | 54.0 | 50.9 | $+78.17 | +3.0% | $1078.17 | +0.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 154 | 55.2 | 51.6 | $+72.50 | +4.7% | $1072.50 | +0.6 | Wed 12:45 PM | too few trades (154/200) |
| value_ev10 | 88 | 43.2 | 39.1 | $+35.25 | +4.0% | $1035.25 | +0.3 | Thu 4:45 AM | too few trades (88/200) |
| value_ev20 | 39 | 35.9 | 35.5 | $-13.85 | -3.6% | $986.15 | -0.2 | Sat 4:00 AM | too few trades (39/200) |
| value_ev5 | 123 | 40.7 | 40.9 | $-61.98 | -5.0% | $938.02 | -0.5 | Wed 6:15 PM | too few trades (123/200) |
| trend_filter | 90 | 44.4 | 49.1 | $-112.79 | -12.5% | $887.21 | -1.2 | Thu 4:00 AM | too few trades (90/200) |
| coinflip | 261 | 50.2 | 51.6 | $-150.64 | -5.8% | $849.37 | -1.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 154 | 44.8 | 49.8 | $-188.70 | -12.3% | $811.30 | -1.5 | Wed 12:45 PM | too few trades (154/200) |
| momentum_60m_0.30pct | 116 | 40.5 | 49.3 | $-218.98 | -18.9% | $781.02 | -2.0 | Wed 7:45 PM | too few trades (116/200) |
| always_up | 261 | 43.7 | 50.0 | $-407.53 | -15.6% | $592.47 | -2.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 347 | 47.0 | 49.6 | $-118.02 |
| ETH | 397 | 45.6 | 48.4 | $-278.83 |
| SOL | 451 | 48.6 | 48.1 | $-252.46 |
| XRP | 468 | 50.2 | 48.3 | $-179.50 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
