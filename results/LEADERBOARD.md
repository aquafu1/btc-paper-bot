# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 2:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 552 windows, 15310 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1306 | 51.4 | 49.7 | $-218.15 | -1.7% | $781.85 | -0.6 | done | can't tell from luck |
| value_ev20 | 301 | 33.2 | 35.2 | $-334.71 | -11.1% | $665.29 | -1.5 | done | can't tell from luck |
| trend_filter | 890 | 50.6 | 51.0 | $-479.63 | -5.4% | $520.37 | -1.7 | done | can't tell from luck |
| value_ev10 | 725 | 37.1 | 39.4 | $-747.98 | -10.3% | $252.02 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1552 | 49.4 | 49.8 | $-801.16 | -5.2% | $198.84 | -2.0 | done | losing for real |
| value_ev5 | 1078 | 39.5 | 41.2 | $-911.26 | -8.5% | $88.74 | -2.4 | done | losing for real |
| reversal_15m_0.10pct | 1552 | 50.6 | 51.2 | $-945.82 | -6.1% | $54.18 | -2.5 | done | losing for real |
| coinflip | 2200 | 50.0 | 50.5 | $-1243.27 | -5.7% | $-243.27 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1306 | 48.6 | 51.2 | $-1324.37 | -10.1% | $-324.37 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2200 | 50.2 | 51.8 | $-1592.52 | -7.2% | $-592.52 | -3.5 | done | losing for real |
| always_up | 2200 | 46.7 | 49.9 | $-2430.52 | -11.0% | $-1430.52 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3463 | 47.5 | 49.2 | $-2825.13 |
| ETH | 3816 | 47.9 | 48.6 | $-2746.73 |
| SOL | 3995 | 47.7 | 48.7 | $-3090.60 |
| XRP | 4036 | 48.5 | 48.6 | $-2366.92 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
