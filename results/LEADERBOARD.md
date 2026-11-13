# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 4:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 224 windows, 5855 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 579 | 56.1 | 52.7 | $+200.96 | +3.5% | $1200.96 | +0.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 455 | 54.9 | 52.5 | $+66.78 | +1.5% | $1066.78 | +0.3 | done | can't tell from luck |
| value_ev20 | 108 | 34.3 | 37.0 | $-125.89 | -11.7% | $874.11 | -1.0 | Sun 7:30 AM | too few trades (108/200) |
| value_ev10 | 291 | 37.8 | 41.0 | $-331.85 | -11.4% | $668.15 | -1.7 | done | can't tell from luck |
| trend_filter | 303 | 44.9 | 50.1 | $-422.79 | -14.0% | $577.21 | -2.5 | done | losing for real |
| value_ev5 | 421 | 39.7 | 42.7 | $-452.74 | -10.8% | $547.26 | -2.0 | done | can't tell from luck |
| momentum_5m_0.00pct | 888 | 50.6 | 51.5 | $-495.84 | -5.6% | $504.16 | -1.7 | done | can't tell from luck |
| coinflip | 888 | 49.7 | 51.0 | $-585.78 | -6.6% | $414.22 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 455 | 45.1 | 49.7 | $-600.01 | -13.2% | $399.99 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 579 | 43.9 | 49.6 | $-866.31 | -15.0% | $133.69 | -3.6 | done | losing for real |
| always_up | 888 | 47.0 | 50.3 | $-945.16 | -10.6% | $54.84 | -3.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1311 | 46.5 | 49.7 | $-1291.04 |
| ETH | 1457 | 46.7 | 49.0 | $-1378.38 |
| SOL | 1513 | 47.9 | 49.4 | $-1233.66 |
| XRP | 1574 | 49.4 | 49.3 | $-655.56 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
