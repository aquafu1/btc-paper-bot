# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 3:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 988 windows, 27461 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 503 | 34.4 | 34.9 | $-265.26 | -5.3% | $734.74 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2804 | 51.1 | 50.4 | $-818.93 | -2.9% | $181.07 | -1.5 | done | can't tell from luck |
| value_ev10 | 1255 | 37.6 | 39.1 | $-861.38 | -6.9% | $138.62 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 2359 | 49.9 | 49.8 | $-1054.04 | -4.5% | $-54.04 | -2.2 | done | losing for real |
| trend_filter | 1646 | 49.6 | 50.9 | $-1192.65 | -7.2% | $-192.65 | -3.0 | done | losing for real |
| value_ev5 | 1899 | 39.5 | 41.0 | $-1248.73 | -6.6% | $-248.73 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2359 | 50.1 | 50.9 | $-1553.27 | -6.6% | $-553.27 | -3.3 | done | losing for real |
| coinflip | 3944 | 50.3 | 50.3 | $-1751.19 | -4.4% | $-751.19 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2804 | 48.9 | 50.3 | $-1937.70 | -6.9% | $-937.70 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 3944 | 50.9 | 51.5 | $-2044.00 | -5.2% | $-1044.00 | -3.4 | done | losing for real |
| always_up | 3944 | 46.7 | 49.6 | $-3996.40 | -10.1% | $-2996.40 | -6.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6262 | 48.2 | 49.1 | $-3522.20 |
| ETH | 6825 | 48.0 | 48.5 | $-4484.45 |
| SOL | 7173 | 48.1 | 48.6 | $-4213.81 |
| XRP | 7201 | 48.1 | 48.5 | $-4503.06 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
