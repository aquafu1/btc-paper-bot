# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 8:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 675 windows, 18687 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 350 | 34.9 | 35.1 | $-174.96 | -5.0% | $825.04 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1590 | 50.6 | 49.6 | $-364.53 | -2.3% | $635.47 | -0.9 | done | can't tell from luck |
| value_ev10 | 862 | 38.7 | 39.3 | $-445.56 | -5.2% | $554.44 | -1.2 | done | can't tell from luck |
| trend_filter | 1090 | 50.5 | 50.9 | $-542.53 | -5.0% | $457.47 | -1.7 | done | can't tell from luck |
| value_ev5 | 1297 | 40.9 | 41.2 | $-590.92 | -4.6% | $409.08 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1916 | 51.3 | 50.9 | $-655.93 | -3.4% | $344.07 | -1.5 | done | can't tell from luck |
| coinflip | 2692 | 50.2 | 50.4 | $-1147.77 | -4.3% | $-147.77 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 1916 | 48.7 | 50.0 | $-1170.61 | -6.1% | $-170.61 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1590 | 49.4 | 51.3 | $-1272.90 | -8.0% | $-272.90 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 2692 | 50.8 | 51.8 | $-1421.00 | -5.3% | $-421.00 | -2.8 | done | losing for real |
| always_up | 2692 | 47.4 | 49.7 | $-2317.55 | -8.6% | $-1317.55 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4251 | 48.3 | 49.2 | $-2423.04 |
| ETH | 4661 | 48.3 | 48.6 | $-2680.26 |
| SOL | 4863 | 48.2 | 48.7 | $-2707.55 |
| XRP | 4912 | 48.5 | 48.5 | $-2293.40 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
