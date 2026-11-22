# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 9:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1061 windows, 29351 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 547 | 34.6 | 35.1 | $-310.90 | -5.7% | $689.10 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2972 | 51.2 | 50.4 | $-808.64 | -2.7% | $191.36 | -1.5 | done | can't tell from luck |
| value_ev10 | 1357 | 37.7 | 39.2 | $-953.77 | -7.0% | $46.23 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2493 | 49.7 | 49.6 | $-1169.22 | -4.7% | $-169.22 | -2.3 | done | losing for real |
| trend_filter | 1748 | 49.4 | 50.7 | $-1327.69 | -7.6% | $-327.69 | -3.3 | done | losing for real |
| value_ev5 | 2061 | 39.6 | 41.0 | $-1359.54 | -6.6% | $-359.54 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2493 | 50.3 | 51.0 | $-1576.92 | -6.3% | $-576.92 | -3.2 | done | losing for real |
| coinflip | 4236 | 50.5 | 50.3 | $-1715.40 | -4.0% | $-715.40 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2972 | 48.8 | 50.3 | $-2056.61 | -6.9% | $-1056.61 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4236 | 50.8 | 51.5 | $-2214.60 | -5.2% | $-1214.60 | -3.5 | done | losing for real |
| always_up | 4236 | 47.2 | 49.4 | $-3730.00 | -8.8% | $-2730.00 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6695 | 48.3 | 49.0 | $-3481.84 |
| ETH | 7262 | 48.1 | 48.5 | $-4605.80 |
| SOL | 7660 | 48.1 | 48.5 | $-4476.45 |
| XRP | 7734 | 48.2 | 48.3 | $-4659.21 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
