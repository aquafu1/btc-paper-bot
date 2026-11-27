# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 10:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1594 windows, 38666 settled trades, 405 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 815 | 34.5 | 35.1 | $-585.00 | -7.2% | $415.00 | -1.6 | done | can't tell from luck |
| value_ev10 | 1924 | 38.5 | 39.0 | $-1019.67 | -5.3% | $-19.67 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3817 | 50.9 | 50.0 | $-1023.04 | -2.7% | $-23.04 | -1.6 | done | can't tell from luck |
| value_ev5 | 2887 | 40.5 | 41.0 | $-1460.38 | -5.1% | $-460.38 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3198 | 51.1 | 50.9 | $-1466.27 | -4.6% | $-466.27 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3198 | 48.9 | 49.2 | $-1735.71 | -5.4% | $-735.71 | -3.1 | done | losing for real |
| trend_filter | 2273 | 48.4 | 50.3 | $-2036.82 | -9.0% | $-1036.82 | -4.4 | done | losing for real |
| coinflip | 5579 | 50.1 | 49.9 | $-2298.56 | -4.1% | $-1298.56 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3817 | 49.1 | 50.2 | $-2341.64 | -6.1% | $-1341.64 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5579 | 50.1 | 51.3 | $-3514.03 | -6.3% | $-2514.03 | -4.8 | done | losing for real |
| always_up | 5579 | 48.2 | 49.1 | $-3567.75 | -6.4% | $-2567.75 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10273 | 48.0 | 48.6 | $-5815.50 |
| ETH | 11083 | 48.0 | 47.7 | $-5649.15 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
