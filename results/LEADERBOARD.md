# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 6:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1289 windows, 34483 settled trades, 419 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 679 | 33.9 | 35.3 | $-569.22 | -8.4% | $430.78 | -1.7 | done | can't tell from luck |
| value_ev10 | 1658 | 38.6 | 39.2 | $-840.94 | -5.1% | $159.06 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3460 | 50.7 | 50.2 | $-1129.81 | -3.3% | $-129.81 | -1.9 | done | can't tell from luck |
| value_ev5 | 2505 | 40.4 | 41.1 | $-1308.63 | -5.2% | $-308.63 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2889 | 49.5 | 49.4 | $-1352.62 | -4.7% | $-352.62 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2889 | 50.5 | 51.0 | $-1635.21 | -5.7% | $-635.21 | -3.1 | done | losing for real |
| trend_filter | 2039 | 49.0 | 50.5 | $-1638.41 | -8.0% | $-638.41 | -3.7 | done | losing for real |
| momentum_15m_0.10pct | 3460 | 49.3 | 50.3 | $-2111.20 | -6.1% | $-1111.20 | -3.6 | done | losing for real |
| coinflip | 4968 | 50.0 | 50.1 | $-2259.64 | -4.5% | $-1259.64 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4968 | 50.5 | 51.4 | $-2763.61 | -5.6% | $-1763.61 | -4.0 | done | losing for real |
| always_up | 4968 | 47.9 | 49.3 | $-3616.69 | -7.3% | $-2616.69 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8262 | 48.0 | 48.8 | $-4820.32 |
| ETH | 8911 | 48.2 | 48.2 | $-4821.43 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
