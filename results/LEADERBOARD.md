# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 9:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 580 windows, 16058 settled trades, 40 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1362 | 51.1 | 49.6 | $-264.12 | -1.9% | $735.88 | -0.7 | done | can't tell from luck |
| value_ev20 | 315 | 33.0 | 35.2 | $-364.56 | -11.6% | $635.44 | -1.6 | done | can't tell from luck |
| trend_filter | 930 | 50.4 | 51.0 | $-510.69 | -5.5% | $489.31 | -1.7 | done | can't tell from luck |
| value_ev10 | 755 | 37.4 | 39.4 | $-737.94 | -9.8% | $262.06 | -2.2 | done | losing for real |
| reversal_15m_0.10pct | 1634 | 51.1 | 51.0 | $-739.56 | -4.5% | $260.44 | -1.9 | done | can't tell from luck |
| value_ev5 | 1127 | 39.8 | 41.3 | $-883.91 | -7.8% | $116.09 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1634 | 48.9 | 49.9 | $-1026.84 | -6.3% | $-26.84 | -2.6 | done | losing for real |
| coinflip | 2313 | 49.9 | 50.5 | $-1221.45 | -5.3% | $-221.45 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1362 | 48.9 | 51.3 | $-1302.87 | -9.6% | $-302.87 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 2313 | 50.2 | 51.9 | $-1628.88 | -7.0% | $-628.88 | -3.5 | done | losing for real |
| always_up | 2313 | 47.0 | 49.8 | $-2339.31 | -10.1% | $-1339.31 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3649 | 47.8 | 49.2 | $-2705.22 |
| ETH | 4005 | 47.9 | 48.6 | $-2818.67 |
| SOL | 4175 | 47.7 | 48.8 | $-3180.00 |
| XRP | 4229 | 48.5 | 48.6 | $-2316.24 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
